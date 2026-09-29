from pydantic import BaseModel , EmailStr , AnyUrl , Field
from typing import List , Dict , Optional , Annotated

class Patient(BaseModel):
    name : str
    age : int 
    weight : float
    married : bool

patient_info = {'name':'nitish', 'age': '30', 'weight': 75.2, 'married': True}
patient1 = Patient.model_validate(patient_info)

print(patient1)
print(type(patient1))