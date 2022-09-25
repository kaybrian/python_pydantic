from pydantic import BaseModel


class Person(BaseModel):
    '''
    This is a class that defines a person class. 
    takes a username, email and age
     
    '''
    username:str 
    email:str
    age:int 
    
data = {
    "username":"testuser",
    "email":"testuser@example.com",
    "age":23
}


new_person = Person(**data)

print(new_person)