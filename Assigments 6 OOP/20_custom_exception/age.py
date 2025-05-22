
class InvalidAgeError(Exception):
    pass  

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        print("Access granted!")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print("InvalidAgeError:", e)
