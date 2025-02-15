high_income = True
good_income = False
student = False


if high_income and good_income:
    print("Eligible ")
if high_income or good_income:
    print("Eligible ")
else:
    print("Not Eligible")



if not student:
    print ("Eligible ")
else : 
    print ("Not Eligible ")



if(high_income or good_income) and not student:
    print ("Eligible")
else :
    print("Not Eligible")
