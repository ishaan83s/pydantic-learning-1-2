from pydantic import BaseModel , EmailStr , AnyUrl , Field
from typing import List , Dict , Optional , Annotated

# class Student(BaseModel):
#     name: str
#     age: int
#     branch: str

# #ORIGINAL METHOD TO CREATE AN PYDANTIC OBJECT (CREATING BY DICTIONARY)
# # vivaan_dict = {
# #     "name" : "Vivaan",
# #     "age" : 21,
# #     "branch" : "Computer Engineering"
# # }

# # student1 = Student(**vivaan_dict)




# student = Student(
#     name="Ishaan",
#     age=21,
#     branch="Computer Engineering"
# )

# print(student) #WE WERE GETTING A DATA THAT WAS PYTHON MODEL
# print(type(student))

# data = student.model_dump(exclude={"age"}) #WHEN USED model_dump() , WE GOT DICTIONARY AS OUTPUT
# print(data)
# print(type(data))


class Student(BaseModel):
    name: str
    age: int | None = None #THIS IS A TYPE OF DEFAULT VALUE ASSIGN THING OR NONE VALUE I GUESS

student1 = Student(
    name = "ishaan",
    age = None #WE DID THAT TYPE OF DEFAULT VALUE ASSIGN ABOVE BCAUSE WE WANTED TO SET THE VALUE NONE HERE
    #THAT WOULDNT BE POSSIBLE WITH THE HELP OF "Field(Default=None)" Thing

)

data = student1.model_dump(exclude_unset=True)
print(data)