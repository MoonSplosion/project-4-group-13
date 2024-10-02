import pandas as pd
import pickle

class ModelHelper():
    def __init__(self):
        # Load the model and the data during initialization
        self.model = self.load_model()
        self.data = self.load_data()  # Load your DataFrame containing features

    def load_model(self):
        # Load and return the fitted model from the file
        try:
            model = pickle.load(open("final_model2.h5", 'rb'))
            return model
        except FileNotFoundError:
            print("Model file not found.")
            return None
        except Exception as e:
            print(f"An error occurred while loading the model: {e}")
            return None

    def load_data(self):
        # Load the DataFrame containing your data
        try:
            return pd.read_csv("final_model2.csv")  # Adjust to your data source
        except FileNotFoundError:
            print("Data file not found.")
            return None

    def makePredictions(self, Name):
        # Check if model and data are loaded
        if self.model is None or self.data is None:
            raise RuntimeError("Model or data is not loaded properly.")

        # Fetch the row corresponding to the given name
        row = self.data[self.data['Name'] == Name]

        if row.empty:
            raise ValueError("No entry found for the provided name.")

        # Extract feature values
        Base_Exp = row['Base Exp.'].values[0]
        Attack = row['Attack'].values[0]
        Sp_Atk = row['Sp. Atk'].values[0]
        Defense = row['Defense'].values[0]
        Sp_Def = row['Sp. Def'].values[0]
        HP = row['HP'].values[0]

        # Create a DataFrame for inference
        df = pd.DataFrame({
            "Base Exp.": [Base_Exp],
            "Attack": [Attack],
            "Sp. Atk": [Sp_Atk],
            "Defense": [Defense],
            "Sp. Def": [Sp_Def],
            "HP": [HP]
        })

        # Make predictions
        preds = self.model.predict(df)
        
        return preds[0]  # Assuming you want the first prediction value
