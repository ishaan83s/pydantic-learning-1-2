from pydantic import BaseModel , ValidationError

class Product(BaseModel):
    name: str
    price: float

data = {
    "name": "Keyboard",
    "price": "expensive"
}

try: 
    product1 = Product.model_validate(data)

except ValidationError as e :
    print(e.errors())


# So Conceptually : 

# ValidationError
#       │
#       └── errors()
#             │
#             ├── loc   → WHERE? [location]
#             ├── msg   → WHAT went wrong? [error msg]
#             ├── input → WHAT was supplied? [what input]
#             └── type  → WHAT kind of validation failure? [type]