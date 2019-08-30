# Create a class to represent a patient of a doctor's office. The Patient class will accept the following information during initialization

# Social security number
# Date of birth
# Health insurance account number
# First name
# Last name
# Address
# The first three properties should be read-only. First name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name. Address should have a getter and setter.

# cashew = Patient(
#     "097-23-1003", "08/13/92", "7001294103",
#     "Daniela", "Agnoletti", "500 Infinity Way"
#     )

# # This should not change the state of the object
# cashew.social_security_number = "838-31-2256"

# # Neither should this
# cashew.date_of_birth = "01-30-90"

# # But printing either of them should work
# print(cashew.social_security_number)   # "097-23-1003"

# # These two statements should output nothing
# print(cashew.first_name)
# print(cashew.last_name)

# # But this should output the full name
# print(cashew.full_name)   # "Daniela Agnoletti"

#don't need to set or get the first or last name because they will be hidden



class Patient ():

    def __init__(self, first, last, social, birth, account, address):
        self.__social_security_number = social
        self.__date_of_birth = birth
        self.__health_insurance_account = account
        self.__first_name = first
        self.__last_name = last
        self.address = address

#social security number - read-only
    @property #getter
    def social_security_number (self):
        try:
            return self.__social_security_number
        except AttributeError:
            return "111-11-1111"

#date of birth - read-only
    @property #getter
    def date_of_birth (self):
        try:
            return self.__date_of_birth
        except AttributeError:
            return "12-1-1990"

#Health insurance account number - read-only
    @property #getter
    def health_insurance_account (self):
        try:
            return self.__health_insurance_account
        except AttributeError:
            return ""

#full_name
    @property #getter
    def full_name (self):
        try:
            return (f"{self.__first_name} {self.__last_name}")
        except AttributeError:
            return ""

    @property #getter
    def address (self):
        try:
            return self.__address
        except AttributeError:
            return ""

    @address.setter #setter
    def address(self, new_address):
        if type(new_address) is str:
            self. __address = new_address
        else:
            raise TypeError('Please provide a string for the address')


karla = Patient("Karla", "Gallegos","123-45-1234", "08/13/92", "7001294103","500 Huntmere Way")

# This should not change the state of the object
# karla.social_security_number = "838-31-2256"

# Neither should this
# karla.date_of_birth = "01-30-90"

# But printing either of them should work
print(karla.social_security_number)   # "123-45-1234"
print(karla.date_of_birth)
print(f"The patient, {karla.full_name}, lives at {karla.address}.")
print(f"* DOB: {karla.date_of_birth}")
print(f"* SS: {karla.social_security_number}")
print(f"* Account {karla.health_insurance_account}")


# These two statements should output nothing
# print(karla.first_name)
# print(karla.last_name)

# But this should output the full name
print(karla.full_name)





