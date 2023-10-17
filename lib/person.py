#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    
    def __init__(self, name = "", job ="Sales"):
        self.set_name(name)
        self._job = job
    def get_name(self):
        print("retrieving name")
        return self._name
    
    def set_name(self, name):
        if  isinstance(name, str) and 1 <= len(name) <= 25:
            print("Name is valid")
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
            
        
    name = property(get_name, set_name)
    
    def get_job(self):
        print("Retrieving job")
        return self._job
    
    def set_job(self, job):
        if job in APPROVED_JOBS:
            print("Setting job")
            self._job = job
            
        else:
            print("Job must be in list of approved jobs.")
            
    job = property(get_job, set_job)    
        
melvin = Person(name = "", job="Sales")
melvin.name = 0
# melvin.job
melvin.job = "Admin"
print(melvin.job)

