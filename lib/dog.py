#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    
    dog_list = []
    
    def __init__(self, name = "", breed = ""):
        self.__set_dog_name(name)
        # self._name = name 
        self._breed = breed
        
        
        
    def get_dog_name (self):
        print("retrieving name")
        return self._name
    
    def __set_dog_name(self, name):
        if  isinstance(name, str) and 1 <= len(name) <= 25:
            print("Name is valid")
            self._name = name
            
        else:
            print("Name must be string between 1 and 25 characters.")
        
    name = property(get_dog_name, __set_dog_name)
    
    def get_breed(self):
        print("Retrieving breed")
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            print("Setting breed")
            self._breed = breed
            
        else:
            print("Breed must be in list of approved breeds.")
        
    breed = property(get_breed, set_breed)
        
fido = Dog(name = "Fido")
fido = Dog(breed = "Human")
