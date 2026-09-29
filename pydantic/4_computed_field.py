from pydantic import BaseModel , fields , EmailStr , AnyUrl  , computed_field
from typing import Optional , Annotated , List , Dict

class Patient(BaseModel):
    
    name : str
    email : EmailStr
    age : int 
    weight : float #kgs 
    height : float #meters 
    married : bool
    allergies : List[str]
    contact_details : Dict[str,str]


    @computed_field
    @property  #What this property decorator does is it makes bmi (the method) as a class property so its not a method now its a property
    #that can be accessed using patient1.bmi(property)
    def bmi(self) -> float :
        bmi = round(self.weight / (self.height**2),2)
        return bmi

    
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("bmi " , patient.bmi)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'height':1.72, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)