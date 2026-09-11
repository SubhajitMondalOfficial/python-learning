marks = {}

x = int(input("Enter physics marks: "))
marks.update({"physics": x})

y = int(input("Enter Math marks : "))
marks.update({"Math": y})

z = int(input("Enter Chemistry marks: "))
marks.update({"Chemistry": z})

print("Your marks is : ", marks)