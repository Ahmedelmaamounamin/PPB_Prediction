import os
from joblib import load
from rdkit.Chem import Descriptors, Crippen, Lipinski
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from rdkit import Chem
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# ============================
# User should specify file paths here
# ============================
model_path = r""  # Write the full path to 'random_forest_regressor_model.joblib'
scaler_path = r""  # Write the full path to 'scaler.joblib'
pca_path = r""  # Write the full path to 'pca_model.joblib'

# Function to calculate molecular properties
def calculate_properties(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None

    properties = {
        "Molecular_Weight": Descriptors.MolWt(mol),
        "PSA": Descriptors.TPSA(mol),
        "H_Bond_Donors": Lipinski.NumHDonors(mol),
        "H_Bond_Acceptors": Lipinski.NumHAcceptors(mol),
        "Rotatable_Bonds": Lipinski.NumRotatableBonds(mol),
        "Aromatic_Rings": Descriptors.NumAromaticRings(mol),
        "Heavy_Atoms": Descriptors.HeavyAtomCount(mol),
        "logP": Crippen.MolLogP(mol),
        "Mol_Refractivity": Crippen.MolMR(mol),
        "RG": Descriptors.MolWt(mol) / Descriptors.HeavyAtomCount(mol) ** 0.333
    }

    return properties

# Function to load the model and make a prediction
def predict_with_model(smiles):
    # Load pre-trained model, scaler, and PCA
    model = load(model_path)
    scaler = load(scaler_path)
    pca = load(pca_path)

    # Calculate properties using the existing function
    properties = calculate_properties(smiles)

    if properties:
        # Prepare features for prediction
        features = np.array([[
            properties["Molecular_Weight"],
            properties["PSA"],
            properties["H_Bond_Donors"],
            properties["H_Bond_Acceptors"],
            properties["Rotatable_Bonds"],
            properties["Aromatic_Rings"],
            properties["Heavy_Atoms"],
            properties["logP"],
            properties["Mol_Refractivity"],
            properties["RG"]
        ]])

        # Scale the features
        features_scaled = scaler.transform(features)

        # Apply PCA transformation
        features_pca = pca.transform(features_scaled)

        # Make prediction
        PPB = model.predict(features_pca)

        print("\n\nPlasma Protein Binding Predicted =", PPB[0])
    else:
        print("Invalid SMILES code.")

# Example of making a prediction
smile_code = input("Enter a SMILES code: ")
predict_with_model(smile_code)