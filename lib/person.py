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
    
    def __init__(self, name = None, job = None):
        self.set_name(name)
        self.set_job(job)

    def get_name(self):
        print("retrieving name")
        return self.name
    
    def set_name(self, name):
        if name is None:
            pass
        elif  isinstance(name, str) and 1 <= len(name) <= 25:
            print("Name is valid")
            self.name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
            
    def get_job(self):
        return self.job
    
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self.job = job 
        else:
            print("Job must be in list of approved jobs.")
            
# melvin = Person(name = "", job="Sales")
person2 = Person()
person2.job="Benevolent dictator for life"



