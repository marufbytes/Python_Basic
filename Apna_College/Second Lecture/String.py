str1="this is a string"
str2 = 'Maruf Ahammed'
str3 = """This is a string """
str4= "This is a  string.\nWe are creating it in python."
print(str4)

str5 = "Thsi is a string.\t We are doing it in python."
print(str5)

#Concatenation
print(str1+str2)
str6 =(str1+" "+str2)
print(str6)

#Lentgth
print(len(str1+str2))
print(len(str6))

#index
ch=str1[0]
print(ch)

#Slicing
ch2=str1[0:6]
print(ch2)
print(str1[:4]) #0:4
print((str1[5:])) 
print(str1[-4:-1])

#Key word
print(str1.endswith("ng"))
print(str1.capitalize())