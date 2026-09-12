# QS1

# i = 1

# while i <= 100:
#     print(i)
#     i+=1

# PS2

# j = 100

# while j >= 1:
#     print(j)
#     j -= 1


# # Multiplication table n


# n = int(input("Enter a number: "))
# i = 1

# while i <= 10:
#     print(n, "X" ,i, "=", i*n)
#     i += 1


# QS 4

nums = (1, 4, 36, 9, 16, 25, 36, 49, 64, 81, 100, 36)
x = 36 

i = 0

while i < len(nums):
    if(nums[i] == x):
        print("FOUND at index", i)
    else:
        print("Finding...")
    i += 1