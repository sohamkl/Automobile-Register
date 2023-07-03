#car2.py file
from typing import NamedTuple 
import pickle 
import os 
FileLocation = r"C:\Users\Eva\Desktop\car.txt" 
hash_table = {} 
for counter in range(0, 100): 
    hash_table[counter] = "" 
 
 
class Car(NamedTuple): 
    id: str 
    colour: str 
    mileage: float 
    automatic: bool 
 
 
def menu(): 
    print("Welcome access car file") 
    print("1. insert a record") 
    print("2. find a record by providing a search key") 
    choice = int(input("Please choose your choice:")) 
    if choice == 1: 
        car_id = int(input("Please provide an id:")) 
        colour = str(input("Please provide an colour:")) 
        mileage = float(input("Please give the mileage:")) 
        automatic = bool(input("is automatic type in 'True' or 'False'")) 
        car = Car(car_id, colour, mileage, automatic) 
        insert_record(car) 
    elif choice == 2: 
        key = int(input("Please provide a search key:")) 
        find_record(key) 
 
 
def hashing(car_id, size): 
    address = int(car_id) % size 
    return address 
 
 
def insert_record(record): 
    index = hashing(record.id, 100) 
    while hash_table[index] != "": 
        index = index + 1 
        if index > 99: 
            index = 0 
    hash_table[index] = record 
    f = open("car.dat", "rb+") 
    f.seek(index) 
    pickle.dump(record, f) 
    f.close() 
 
 
def find_record(search_key): 
    index = hashing(search_key, 100) 
    while hash_table[index].id != search_key and hash_table[index] != "": 
        index = index + 1 
        if index > 99: 
            index = 0 
    if hash_table[index] != "": 
        return hash_table[index] 
    else: 
        print("not found") 
 
menu()

