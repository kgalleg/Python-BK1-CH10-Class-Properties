# Define a Python class named Student. This class will have 5 properties.

# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string) *****how do you do a read only string?

# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by a space. It's value cannot be set.


class Student:

    def __str__(self):
        return f'My first name is {self.first_name} and my last name is {self.last_name}.  I am {self.age} and in cohort {self.cohort}.  My full name is: {self.full_name}.'


#first name - string
    @property #getter
    def first_name (self):
        try:
            return self.__first_name
        except AttributeError:
            return 0

    @first_name.setter #setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self. __first_name = new_first_name
        else:
            raise TypeError('Please enter your first name')


#last name - string
    @property #getter
    def last_name (self):
        try:
            return self.__last_name
        except AttributeError:
            return 0

    @last_name.setter #setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self. __last_name = new_last_name
        else:
            raise TypeError('Please enter your last name')


#age - integer
    @property #getter
    def age_num (self):
        try:
            return self.__age_num
        except AttributeError:
            return 0

    @age_num.setter #setter
    def age_num(self, new_age_num):
        if type(new_age_num) is int:
            self. __age_num = new_age_num
        else:
            raise TypeError('Please enter your age')


#cohort number - integer
    @property #getter
    def cohort_num (self):
        try:
            return self.__cohort_num
        except AttributeError:
            return 0

    @cohort_num.setter #setter
    def cohort_num(self, new_cohort_num):
        if type(new_cohort_num) is int:
            self. __cohort_num = new_cohort_num
        else:
            raise TypeError('Please enter your cohort number')


#full name - read only string
    @property #getter
    def full_name (self):
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return ""

#I do not need a full_name setter...



# CAN reset attribute
karlita = Student()
karlita.first_name = "Karla"
karlita.last_name = "Gallegos"
karlita.age = 21
karlita.cohort = 100



print(karlita)

# CANNOT reset attribute
karlita.full_name = "blahblah"










# Part two - convert student object to a string was completed above:


# Use the __str__ and __repr__ magic methods on your class to specify what an object's string representation should be. It's just like the toString() method in JavaScript.

# If you print a Student object. The output would look something like below.

# mike = Student()
# mike.first_name = "Mike"
# mike.last_name = "Ellis"
# mike.age = 35
# mike.cohort_number = 39

# print(mike)
# <__main__.Student object at 0x107133f60>
# But if you specify exactly what string should be returned from __str__ or __repr__, that will print out instead. If you implement the following method on your class...

# class Student:

#     def __str__(self):
#         return f"{self.full_name}"
# then the output will change

# print(mike)
# Mike Ellis
# Change your class so that any objects created from it will be rerpesented as strings in the following format.

# Mike Ellis is 35 years old and is in cohort 39



