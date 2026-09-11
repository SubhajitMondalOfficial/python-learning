student = {
    "name": "Subhajit",
    "age": 21,
    "course": "CSE"
}

# keys()
print(student.keys())

# values()
print(student.values())

# items()
print(student.items())

#get()
print(student.get("name"))

# update()
student.update({"age": 22, "course": "IT"})
print(student)