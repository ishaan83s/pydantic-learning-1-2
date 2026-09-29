from pydantic import BaseModel , ConfigDict , Field

class User(BaseModel):
    model_config = ConfigDict(extra="forbid") #Raises ValidationError
    #extra = "ignore" <-- DEFAULT
    #extra = "allow" 

    name: str
    age: int


data = {
    "name": "Ishaan",
    "age": 21,
    "password": "secret123" # <-----
}

user1 = User.model_validate(data)

print(user1) #doesnt print password it clearly ignores it 