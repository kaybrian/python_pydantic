from pydantic import BaseModel, ValidationError, Field, BaseSettings
from typing import List
from enum import Enum
import json

class Gender(str, Enum):
    Male = "Male"
    Female = "Female"
    

class Person(BaseModel):
    '''
    This is a class that defines a person class. 
    takes a username, email and age
    '''
    username:str=Field(default=None, max_length=10, min_length=3)
    email:str=Field(default=None, max_length=20, min_length=8)
    age:int=Field(lt=60,gt=18)
    friends:List[str] = [] 
    gender :Gender
    
    
# here is the correct data for the model,
data = {
    "username":"testuser",
    "email":"testuser@example.com",
    "age":23,
    "friends":["testuser2","testuser3"],
    "gender":Gender.Female
}

# incorrect data fro the model
data2 = {
    "username":"er",
    "email":"testuser@example.com",
    "age":15,
    "friends":["testuser2","testuser3"],
    "gender":Gender.Female
}


# try:
#     new_person = Person(**data)
#     our_schema = new_person.schema()
    
#     print(json.dumps(our_schema, indent=4))
    
# except ValidationError as e:
#     print(e.json())

class Settings(BaseSettings):
    api_key:str 
    
    class Config:
        env_file=".env"
        env_encoding="utf-8"
        
my_settings = Settings()

print(my_settings)