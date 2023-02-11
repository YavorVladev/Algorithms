def bubble_sort(current_list):
    length = len(current_list) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(0, length):
            if current_list[i] > current_list[i + 1]:
                is_sorted = False
                current_list[i], current_list[i + 1] = current_list[i + 1], current_list[i]

    return current_list


a = [1, 4, 3, 2, 5, 8, 7, 6, 11, 9, 10, 15, 12, 13, 16, 18, 17]
print(bubble_sort(a))
