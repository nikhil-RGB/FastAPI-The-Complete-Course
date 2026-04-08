score=int(input("Enter grade"))
grade=""
if score>=90 and score<=100:
    grade="A"
elif score>=80:
    grade="B"
elif score>=70:
    grade="C"
elif score>=60:
    grade="D"
elif score>=0 and score<=59:
    grade="E"
else:
    grade="Invalid"
print(f"grade is {grade}")

    