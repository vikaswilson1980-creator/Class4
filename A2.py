#total amount of note taking an input
amount=int(input("Enter the Amount for withdrawal:"))
#claculating the number of note of different denominations
note1=amount//100
note2=(amount % 100)//50
note3=((amount % 100)% 50)//10
print("You can withdraw note of 100 :",note1)
print("You can withdraw note of 50 :",note2)
print("You can withdraw note of 10 :",note3)