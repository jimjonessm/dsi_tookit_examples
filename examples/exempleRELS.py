from matplotlib.pyplot import (figure, plot, title, xlabel, ylabel, legend, 
                               grid, box, show, subplot, close)
from scipy.io import loadmat
from dsi_toolkit import (generateCandidateTerms, removeClusters, detectStructure,
                 getInfo, estimateParametersRELS, correlationFunction,
                 validateModel, groupcoef, buildStaticResponse,
                 displayStaticModel, correlationCoefficient, displayModel,
                 buildMapping)
from os import system
from scipy.optimize import curve_fit
from numpy import array

# This example of System Identification refers to the Buck-Boost DC-DC Converter
# contained in the work titled: Aguirre, L.A.; BARROSO, M.F.S.; Saldanha, R.R.;
# Mendes, E.M.A.M. "Imposing steady-state performance on identified nonlinear
# polynomial models by means of constrained parameter estimation." IEE Proceedings,
# Control Theory and Applications, UK, v. 151, n. 02, p. 174, 2004.
#
# http://dx.doi.org/10.1049/ip-cta:20040102
#
# In this example, the grey-box identification uses the theoretical static
# curve knowledge of the converter, and the parameters are estimated using
# the restrict extended least squares estimator.
#

# Clear data, close open windows, and clear the command prompt
# --------------------------------------------------------------------------
system('cls')
close('all')

# --------------------------------------------------------------------------
# Load dynamic data
# --------------------------------------------------------------------------
data = loadmat('converter_dataset.mat')
ti = data['ti'].flatten()
ui = data['ui'].flatten()
yi = data['yi'].flatten()
tv = data['tv'].flatten()
uv = data['uv'].flatten()
yv = data['yv'].flatten()
u = data['u'].flatten()
y = data['y'].flatten()

# --------------------------------------------------------------------------
h = figure()
h.canvas.manager.set_window_title('Real Data')
# Subplot with input data
# --------------------------------------------------------------------------
subplot(2, 1, 1)
plot(ti, ui, 'r')
title('Input and Output Data')
plot(tv, uv, 'b')
ylabel('u[k]')
legend(['Identification Data', 'Validation Data'])
grid(True)
box(True)

# --------------------------------------------------------------------------
# Subplot with output data
# --------------------------------------------------------------------------
subplot(2, 1, 2)
plot(ti, yi, 'r')
plot(tv, yv, 'b')
ylabel('y[k]')
xlabel('k[s]')
legend(['Identification Data', 'Validation Data'])
grid(True)
box(True)
show()

# --------------------------------------------------------------------------
# 1 - Generate Candidate Terms Matrix
model, Tterms, type = generateCandidateTerms(1, [8, 8, 4])

# 2 - Detect the Structure:
# 2.1 - Remove inappropriate clusters (knowledge of the static curve)
#model = removeClusters(model, 2, 0)
#model = removeClusters(model, 1, 1)
#model = removeClusters(model, 0, 2)

# 2.2 - Run structure detection algorithms like AIC and ERR
model, _, _, ERR, ERRp, ERRr, mint = detectStructure(model, ui, yi, 5, 5, 1, 1)

# 3 - Estimate Parameters of the Model with Detected Structure
numProcessTerms, numNoiseTerms, maxDelay, maxOutputDelay, maxInputDelay, maxNoiseDelay, processModel, noiseModel, model = getInfo(model)

# 3.1 - Estimate Clusters Coefficients (B) by curvefit
initialCond = [0, 0, 0]
def rationalModel(x, coef1, coef2, coef3):
    return (coef1 + coef3 * x) / (1 - coef2)
B, _ = curve_fit(rationalModel, u, y, p0=initialCond)


A = buildMapping(processModel) # Dynamic and static Parameters Mapping

# Estimation using Restrict Extended Least Square
Parameters, ParametersP, ParametersR, vP, MP, e = estimateParametersRELS(model, ui, yi, 100, A, B)

_, _ = correlationFunction(e, len(e), 1)

# 4 - Validate the dynamic model
yhat, r, R, ev = validateModel(processModel, ParametersP, tv, uv, yv, 1, 1, 1, 0)

# 5 - Obtain the static model and simulate
clusters, coefficients, staticModel, E = groupcoef(processModel, ParametersP)
uest = u

Y, Pest, EstimatedParameters = buildStaticResponse(staticModel, uest, y)

yest, eqest = displayStaticModel(staticModel, uest, 1)

res = correlationCoefficient(y, yest)

# --------------------------------------------------------------------------
figure()
plot(u, y, 'b')
title('Static Data')
plot(uest, yest, 'ro')
xlabel('u', fontsize=10)
ylabel('y', fontsize=10)
legend(['Static', 'Simulated Static'])
grid(True)
box(True)
show()

# --------------------------------------------------------------------------
print('Analysis of the error between real data and the free simulation of the model:')
print(f'The RMSE (R) value is {R.item():.3f}')
print('Analysis of the autocorrelation of validation residuals')
print(f'The Correlation (r) value is {r.item():.3f}')
print('Analysis of the autocorrelation between the static model and static data')
print(f'The Correlation (r) value is {res.item():.3f}')

eqP = displayModel(processModel, ParametersP, 1)
