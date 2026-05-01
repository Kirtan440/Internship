x = input("enter a character: ")

if x == 'a':
    print("You have enter a")
elif x == 'b':
    print("You have enter b")
elif x == 'c':
    print("You have enter c")
else:
    print("invalid character")



a = int(input("enter a number: "))

if a > 0:

    if a % 2 == 1:
        result = a + 5 
        print("Addition result is", result) 
        print("a is odd and positive")
    else:
        result = a * 2.5
        print("Multiplication result is", result)
        print("a is even and positive")  

if a < 0:

    if a % 2 == 1:
        result = a - 5 
        print("Subtraction result is", result) 
        print("a is odd and negative")
    else:
        result = a / 2.5
        print("Division result is", result)
        print("a is even and negative")     


marks = int(input("enter your marks: "))
if marks <= 100 and marks >= 90:
    print("Grade A")
elif marks < 90 and marks >= 80:
    print("Grade B")
elif marks < 80 and marks >= 60:
    print("Grade C")
elif marks < 60 and marks >= 40:
    print("Grade D")
elif marks < 40 :
    print("Fail")
else:
    print("Invalid marks")

