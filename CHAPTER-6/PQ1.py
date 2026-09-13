def LenList(list):
    print(len(list))
    return len(list)

def printList(list):
    for item in list:
        print(item, end=" ")

numbers = [10, 20, 30, 40, 50]
LenList(numbers)
printList(numbers)