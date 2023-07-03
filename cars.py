from typing import NamedTuple  

import pickle 


class Car(NamedTuple):  

    id : str 

    colour: str  

    mileage: float  

    automatic: bool  

cars = [None] *50
hashtable = [None] * 100
def Insert(record):  
        
    index = hash(record.key)      
    while hashtable[index] != " ":
        index += 1
        if index > max:
            index = 1

        hashtable[index] = record 

c1 = Car(id="23344",colour="Black",mileage=234.5,automatic=True)
Insert(c1.key)

