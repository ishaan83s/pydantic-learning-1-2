
from pydantic import BaseModel , ConfigDict , Field

class User(BaseModel):
    model_config = ConfigDict(strict=True) #THIS MAKES TYPE COERSION STRICT FOR WHOLE MODEL NOT
    #JUST A FIELD

    name: str
    age: int  # age: int = Field(strict= True) , STRICT CAN ALSO BE DONE LIKE THIS


data = {
    "name": "Ishaan",
    "age": "21",
    "password": "secret123" # <-----
}

user1 = User.model_validate(data)

print(user1) #doesnt print password it clearly ignores it 