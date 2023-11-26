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
    def __init__(self, name, job=None):
        self._name = None
        self._job = None
        self.set_name(name)
        self.set_job(job)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 0 < len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    def get_job(self):
        return self._job

    def set_job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)
    

