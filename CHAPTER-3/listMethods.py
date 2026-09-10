# Appending an element to the list

list = [10, 20, 40, 50,  30]
print("Original list:", list)
list.append(60)
print("Updated list:", list)

# Sorting a list in ascending order
list.sort()
print("Sorted list:", list)

# Sorting a list in descending order
list.sort(reverse=True)
print("Sorted list in descending order:", list)

# Sorting a list using the reverse() method
list.reverse()  
print("Reversed list:", list)

# Inserting an element at index 2
list.insert(2, 25) 
print("List after inserting 25 at index 2:", list)

# Removing an element from the list
list.remove(60)
print("List after removing 60:", list)

# Removing an ekement using the pop() method
list.pop(3) 
print("List after popping element at index 3:", list)