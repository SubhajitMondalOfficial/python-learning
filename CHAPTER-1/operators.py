# Arithmetic Operators
first_number = 10
second_number = 3

print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)
print("Division:", first_number / second_number)
print("Modulus:", first_number % second_number)
print("Floor Division:", first_number // second_number)
print("Exponent:", first_number ** second_number)


# Comparison Operators
print("Equal:", first_number == second_number)
print("Not Equal:", first_number != second_number)
print("Greater Than:", first_number > second_number)
print("Less Than:", first_number < second_number)
print("Greater Than or Equal:", first_number >= second_number)
print("Less Than or Equal:", first_number <= second_number)


# Assignment Operators
number = 10
number += 5
print("After +=:", number)

number -= 3
print("After -=:", number)

number *= 2
print("After *=:", number)


# Logical Operators
age = 20
has_id = True

print("AND:", age >= 18 and has_id)
print("OR:", age >= 18 or has_id)
print("NOT:", not has_id)


# Identity Operators
first_list = [1, 2, 3]
second_list = first_list

print("Same Object:", first_list is second_list)
print("Different Object:", first_list is not second_list)


# Membership Operators
fruits = ["apple", "banana", "mango"]

print("Apple exists:", "apple" in fruits)
print("Orange does not exist:", "orange" not in fruits)


# Bitwise Operators
first_number = 5
second_number = 3

print("Bitwise AND:", first_number & second_number)
print("Bitwise OR:", first_number | second_number)
print("Bitwise XOR:", first_number ^ second_number)
print("Bitwise NOT:", ~first_number)
print("Left Shift:", first_number << 1)
print("Right Shift:", first_number >> 1)