# DSI Toolkit Examples

## Overview
The **DSI Toolkit** (Dynamic System Identification Toolkit) provides various functions for system identification, model validation, and regression analysis. This package is designed for researchers and engineers working with polynomial models and system dynamics.

## Installation

### **Using pip**
To install the DSI Toolkit, run:
```bash
pip install dsi-toolkit
```

### **Using Conda**
If using Conda, install it via pip inside a Conda environment:
```bash
conda create --name dsi_env python=3.9
conda activate dsi_env
pip install dsi-toolkit
```

## Usage

See the examples.

## Functions
### **Main Functions**
1. `generateCandidateTerms`: Generates candidate terms for the model.
2. `getInfo`: Obtains information about the model.
3. `detectStructure`: Detects the model structure.
4. `buildRegressorMatrix`: Constructs the regressors' matrix.
5. `rmse`: Calculates the RMSE error.
6. `delay`: Produces a delayed signal in discrete time.
7. `combinationWithRepetition`: Calculates term combinations with repetition.
8. `removeClusters`: Removes inappropriate term groupings.
9. `validateModel`: Validates the model.
10. `correlationFunction`: Calculates and displays the correlation function.
11. `correlationCoefficient`: Computes the correlation coefficient.
12. `buildStaticResponse`: Generates the model's static response.
13. `groupcoef`: Calculates term grouping coefficients.
14. `buildMapping`: Maps dynamic parameters to term grouping coefficients.
15. `estimateParametersELS`: Estimates parameters using Least Squares.
16. `estimateParametersRELS`: Estimates parameters using Restricted Least Squares.
17. `displayModel`: Displays the model in text and graphical form.
18. `displayStaticModel`: Displays the static model.
19. `checkSubarrayForGNLY`: Detects the degree of nonlinearity in clusters.

## Contributing
Feel free to open an issue or submit a pull request if you would like to contribute.

## License
This package is licensed under a proprietary license. For commercial use or permissions, contact: **barrosos@ufsj.edu.br**

## Cite as
Barroso, M. F. S, Mendes, E. M. A. M. and Marciano, J. J. S. (2025). Dynamic Systems Identification (Polynomial Models) (https://pypi.org/project/dsi-toolkit/), pypi.org. Retrieved March 16, 2025.

## Contact
For questions or support, please contact:
📧 **barrosos@ufsj.edu.br**
