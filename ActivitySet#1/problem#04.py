# Conditional Execution
def grade(s):
    if(s > 0 and s < 1):
        if(s >= 0.9):
            print("A")
        elif(s >= 0.8):
            print("B")
        elif(s >= 0.7):
            print("C")
        elif(s >= 0.6):
            print("D")
        else:
            print("F")
    else:
        print("not a score")
 
s = float(input("Enter the score: "))
grade(s)

