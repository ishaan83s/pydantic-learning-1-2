from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pin : str

class Patient(BaseModel):

    name : str
    age : int
    address : Address

address_dict = {
    "city" : "Pune",
    "state" : "Maharashtra",
    "pin" : "3088812"
}

address_1 = Address(**address_dict)

# #    name : str
#     age : int
#     address : Address

patient_dict = {
    "name" : "ritik",
    "age" : "21",
    "address" : address_1
}



# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed