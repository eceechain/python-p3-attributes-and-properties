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
    def __init__(self, name='fido', breed="Mastiff"):
        self.breed = breed
        self.name = name

    def set_name(self, value):  # Added set_name method
        if type(value) == str and 0 < len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_name(self):  # Added get_name method
        return self._name


    name = property(get_name, set_name)  # Using property() to define name property

    def get_breed(self):  # Added get_breed method
        return self._breed

    def set_breed(self, value):  # Added set_breed method
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)  # Using property() to define breed property
    
