def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i

        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    return arr


a = [1, 4, 3, 2, 5, 8, 6, 7]
print(insertion_sort(a))
