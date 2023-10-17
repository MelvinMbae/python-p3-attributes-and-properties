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
    
    def __init__(self, name = None, breed = None):
        self.__set_dog_name(name)
        self.__set_breed(breed)      
        
    def get_dog_name (self):
        print("retrieving name")
        return self.name
    
    def __set_dog_name(self, name):
        if name is None:
            self.name = name
        elif isinstance(name, str) and 1 <= len(name) <= 25:
            print("Name is valid")
            self.name = name     
        else:
            print("Name must be string between 1 and 25 characters.")
        
    
    def get_breed(self):
        print("Retrieving breed")
        return self.breed
    
    def __set_breed(self, breed):
        if breed is None:
            self.breed = None
        elif breed in APPROVED_BREEDS:
            print("Setting breed")
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")
        
    # breed = property(get_breed, __set_breed)
        
fido = Dog(name = "Fido")
fido = Dog(breed = "Human")
