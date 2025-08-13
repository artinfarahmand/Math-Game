import random
number= int(input("Enter a number from 1 to 9:"))
step1= number*2
step2= step1+8
step3= step2 + number
step4= step3 - 2
step5= step4 / 3
step6= step5 - number
step7= step6 * 4
print(f"The answer should be 8: {step7}")