import sys
print("BODY MASS INDEX CALCULATOR\n")
w = input("What's your weight in lbs:\n")
h = input("What's your height in inches:\n")
bmi = ((703 * float(w)) / (float(h) * float(h)) )
print("Your Body-Mass-Index is :\n"+str(bmi))