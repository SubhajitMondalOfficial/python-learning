# Check if a list is a  palindrome or not

list = [1, 2, 3, 2, 1]

reverse_list = list.reverse()

if list == reverse_list:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")