listt = []
listt = (input("Enter the list : ")).split()
print(listt)

copyList = listt.copy()
copyList.reverse()

if(copyList == listt):
    print("Palndrome")

else:
    print("Nnot palindrome")
