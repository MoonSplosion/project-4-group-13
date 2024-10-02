import pandas as pd
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(self, Name, Type, Species, Height, Abilities, Catch_Rate, Weight, Base_Friendship, Base_Exp, Growth_Rate):
        # create dataframe of one row for inference
        df = pd.DataFrame()
        df["Name"] = [Name]
        df["Type"] = [Type]
        df["Species"] = [Species]
        df["Height"] = [Height]
        df["Weight"] = [Weight]
        df["Abilities"] = [Abilities]
        df["Catch_Rate"] = [Catch_Rate]
        df["Base_Friendship"] = [Base_Friendship]
        df["Base_Exp"] = [Base_Exp]
        df["Growth_Rate"] = [Growth_Rate]

        # model
        model = pickle.load(open("titanic_model_pipeline2.h5", 'rb'))

        # columns in order
        df = df.loc[:, ['Abilities', 'Name', 'Type', 'Species', 'Catch_Rate', 'Height', 'Weight', 'Base_Friendship', 'Base_Exp', 'Growth_Rate']]

        preds = model.predict_proba(df)
        return(preds[0][1])
