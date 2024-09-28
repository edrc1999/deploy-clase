from fastapi import FastAPI
import pickle
from Diabetesdata import DiabetesData
app = FastAPI()

pkl_filename = "RFDiabetesv102.pkl"
with open(pkl_filename, "rb") as file:
    model = pickle.load(file)
    
labels = ["Sano", "Diabetes"]
    
@app.get("/")
async def root():
    return{
        "message":"AI service"
    }
    
@app.post("/predict")   
def predict_diabetes(data:DiabetesData):
    data = data.model_dump()
    Pregnancies = data["Pregnancies"]
    Glucose = data ["Glucose"]
    BloodPreassure = data["BloodPreassure"]
    SkinThickness = data["kinThickness"]
    Insulin = data["Insulin"]
    BMI = data["BMI"] 
    DiabetesPedigreefunction = data[DiabetesPedigreefunction]
    Age = data[Age]
    
    return {
        "Age":Age
    }
    
    