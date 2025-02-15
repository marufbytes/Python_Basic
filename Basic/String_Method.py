course = 'Python for Beginners'
print ('Length : ', len(course))
print("UPPER : ",course.upper())
print("Lower : ",course.lower())
print ("Index Number : ", course.find('P')) #case sensetive
print ("Index Number : ", course.find('Beginners'))
print ("Index Number : ", course.find('p'))
print ("Index Number : ", course.find('beginners'))
print ('Replaced : ',course.replace('Beginners', 'Absolute Beginners'))
print ('Existance : ' ,'Python' in course) #Bool
