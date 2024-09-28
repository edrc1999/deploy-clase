from pydantic import BaseModel

class  DiabetesData(BaseModel):
    Pregnancies:int 
    Glucose: int
    BloodPreassure:int 
    kinThickness: int 
    Insulin:int
    BMI:float 
    Age:int
    DiabetesPedigreefunction:float
    