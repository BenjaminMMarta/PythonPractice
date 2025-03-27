# Create Person Class
class Person:
    #Initializing Person Class With First Name, Last Name, Age, Birthdate, and Hometown. 
    def __init__(self, first_name, last_name, age, birthdate, hometown):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birthdate = birthdate
        self.hometown = hometown

    #Adding String Method To Print Out Person Details In String Format
    def __str__(self):
        return f"{self.first_name} {self.last_name} is from {self.hometown}. {self.first_name} is {self.age} years old. {self.first_name}'s birthdate is {self.birthdate}!"


benjamin_marta = Person("Benjamin", "Marta", "41", "November 3rd, 1983", "San Diego, CA")

print(benjamin_marta)

