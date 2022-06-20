def merge(left_arr, right_arr):
    i,j = 0,0
    sorted_arr = []
    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i] <= right_arr[j]:
            sorted_arr.append(left_arr[i])
            i += 1
        else:
            sorted_arr.append(right_arr[j])
            j += 1
    sorted_arr += left_arr[i:]
    sorted_arr += right_arr[j:]
    return sorted_arr

def mergeSort(arr):
    print(arr)
    if len(arr) <= 1:
        return arr
    else:
        mpt = int(len(arr)/2)
        left_arr = mergeSort(arr[:mpt])
        right_arr = mergeSort(arr[mpt:])
        print(left_arr, right_arr)
        return merge(left_arr, right_arr)

def main():
    list = [4, 1, 76, 42, 51, 61, 9, 21, 89, 7, 11, 20, 4, 2, 4]
    print(mergeSort(list))

if __name__ == '__main__':
    main()