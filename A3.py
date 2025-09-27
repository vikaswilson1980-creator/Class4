#take marks a input from user
print("Enter marks optained in 4 subjects:")
maths=int(input("Enter your marks:")) 
Science=int(input("Enter your marks:")) 
Social=int(input("Enter your marks:"))
Hindi=int(input("Enter your marks:"))
#lets calculate the persentage of marks
sum=maths+Science+Social+Hindi
print("THe sum of Maths,Science, Social and Hindi:",sum)
perc=(sum/400)*100
print("the percentage of all the subjects are:",perc)