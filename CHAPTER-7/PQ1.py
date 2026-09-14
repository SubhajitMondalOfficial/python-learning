# with open("practice.txt", "a+") as f:
#     f.write("Hi everyone\nwe are learing File I/O\nusing Java.\nI like programming in Java")


# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)


# ==== find if the given string is availavle or not  =====

# word = "learning"

# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")


# ===In which line word occur first====

def chack_for_line():
    word = "learning"
    data = True
    line_no = 1

    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1

    return -1
j
chack_for_line()