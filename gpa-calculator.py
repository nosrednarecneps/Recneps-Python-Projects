grade = int(input("Gimme a grade!: "))
if grade >= 94:
    print("GPA: 4.0 or A")
elif grade >= 90:
    print("GPA: 3.7 or A-")
elif grade >= 87:
    print("GPA: 3.3 or B+")
elif grade >= 83:
    print("GPA: 3.0 or B")
elif grade >= 80:
    print("GPA: 2.7 or B-")
elif grade >= 77:
    print("GPA: 2.3 or C+")
elif grade >= 73:
    print("GPA: 2.0 or C")
elif grade >= 70:
    print("GPA: 1.7 or C-")
elif grade >= 67:
    print("GPA: 1.3 or D+")
elif grade >= 60:
    print("GPA: 1.0 or D")
elif grade < 60: 
    print("GPA: 0.0 or F")
else:
    print("Really?")