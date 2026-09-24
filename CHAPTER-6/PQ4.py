def print_list(list, idx):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)


print([1, 2, 3, 4, 5, 6])