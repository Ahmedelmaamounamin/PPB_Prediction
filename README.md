# Plasma Protein Binding Prediction Software

## Overview
This open-source software predicts the **Plasma Protein Binding (PPB)** percentage from a given **SMILES** string using a **pre-trained Random Forest Regressor model**. The model utilizes molecular descriptors calculated using **RDKit**.

## Requirements
### 1. Install Dependencies
Ensure you have the required Python libraries installed. You can install them using:

```bash
pip install numpy pandas scikit-learn joblib rdkit requests
```


### 2. Required Files
To run this tool, you must have the following files:


# Pre-trained Model
- **random_forest_regressor_model.joblib**
  - 📥 **Download it from [PPB_Prediction_Software_GitHub Releases](https://github.com/Ahmedelmaamounamin/PPB_Prediction/releases/download/PPB_Software/random_forest_regressor_model.joblib)**
  - Save it to your local machine and specify its path in the script.

# Included with the Repository
- **scaler.joblib** (StandardScaler object for feature scaling)
- **pca_model.joblib** (PCA model for dimensionality reduction)


## How to Use

1. Open the Python script (`main.py`).
2. Locate the section:

   model_path = r""  # Provide the full path to 'random_forest_regressor_model.joblib'
   scaler_path = r"scaler.joblib"  # Pre-included in the repository
   pca_path = r"pca_model.joblib"  # Pre-included in the repository

3. Replace `model_path` with the **full path** to your downloaded model file.
4. Run the script:

   main.py

5. Enter a **SMILES string** when prompted.
6. The software will output the predicted **Plasma Protein Binding (PPB)** percentage.


## Example Run

Enter a SMILES code: O=C1C(NS(=O)(=O)/C=C/c2ccc(Cl)s2)CCN1c1ccc(-n2ccnc2CN2CCCC2)cc1F

Plasma Protein Binding Predicted = 92.16


## Notes

- Ensure that the SMILES input is valid.
- If you encounter errors related to missing dependencies, install them using `pip install` as mentioned above.


## License

This software is **open-source** and released under the **MIT License**.
