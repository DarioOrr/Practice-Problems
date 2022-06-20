def quickSort(arr):
    print(arr)
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left_arr = [i for i in arr[1:] if i <= pivot]
        right_arr = [i for i in arr[1:] if i > pivot]
        return quickSort(left_arr) + [pivot] + quickSort(right_arr)

def main():
    list = [4, 1, 76, 42, 51, 61, 9, 21, 89, 7, 11, 20, 4, 2, 4]
    print(quickSort(list))

if __name__ == '__main__':
    main()