try:
    age = int(input("Age : "))
    print(age)
    income = 200000
    risk = income/age

except ZeroDivisionError:
    print('Age can not be zero')

except ValueError:
    print("Invalid value")



