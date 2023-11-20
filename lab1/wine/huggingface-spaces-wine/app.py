import gradio as gr
from PIL import Image
import requests
import hopsworks as hw
import joblib
import pandas as pd
import xgboost as xgb

project = hw.login(project="jayeshv")
fs = project.get_feature_store()

mr = project.get_model_registry()
model = mr.get_model("wine_model", version=2)
model_dir = model.download()

model = joblib.load(model_dir+'/wine_model.pkl')
print("Model Loaded...")

def wine(type,
         fixed_acidity,
         volatile_acidity,
         citric_acid,
         residual_sugar,
         chlorides,
         free_sulfur_dioxide,
         total_sulfur_dioxide,
         density,
         ph,
         sulphates,
         alcohol):
    print("Lets taste wine?")
    
    df = pd.DataFrame([[type, fixed_acidity, volatile_acidity,
                        citric_acid, residual_sugar,
                        chlorides, free_sulfur_dioxide,
                        total_sulfur_dioxide,
                        density, ph, sulphates, alcohol]],
                      columns = ['type', 'fixed_acidity', 'volatile_acidity',
                                 'citric_acid', 'residual_sugar', 'chlorides',
                                 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
                                 'ph', 'sulphates', 'alcohol'])
    
    print("Predicting...")
    
    res = model.predict(df)
    print(res)
    
    return res

demo = gr.Interface(
    fn = wine,
    title = 'Wine Quality prediction',
    description = '',
    allow_flagging = 'never',
    inputs = [
        gr.Number(value=0, label="type"),
        gr.Number(value=6.3, label="fixed_acidity"),
        gr.Number(value=0.30, label="volatile_acidity"),
        gr.Number(value=0.49, label="sulphates"),
        gr.Number(value=9.5, label="alcohol"),
        gr.Number(value=0.994, label="density")
    ],
    outputs="number" # output's an integer from 3-9
)

demo.launch(debug=True)
