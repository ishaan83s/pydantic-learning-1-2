from pydantic import BaseModel, ConfigDict, Field , ValidationError

#from_attributes=True lets Pydantic read data from object attributes rather than requiring dictionary-style input.

#ASSUME THIS IS A RECORD THAT WE NEED TO VALIDATE USING PYDANTIC
#BUT SINCE IT IS NOT IN A FORMAT THAT PYDANTIC GENERALLY KNOWS TO 
#VALIDATE FROM , THEREFORE WE USE from_attributes = True
#THIS MEANS WE CAN CREATE A PYDANTIC MODEL FROM ANY CLASS ATTRIBUTES
#FOR EG :


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name : str
    age : int

#we cant do user1 = User.model_validate(UserRecord) if we dont use
#from_attributes because its not a dict
#and similarly we cannot use _json
class UserRecord:
    name = "Ishaan"
    age = 21

user1 = UserRecord()

try :
    user1 = User.model_validate(user1)
except ValidationError as e:
    print(e.errors())

print(user1)


