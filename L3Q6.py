def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def switch_case(option, arr):
    switcher = {
        1: bubble_sort,
        2: merge_sort,
        3: selection_sort,
        4: insertion_sort
    }
    sort_func = switcher.get(option, lambda x: "Invalid option")
    return sort_func(arr)

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Enter the number corresponding to the sorting algorithm you want to use:")
    print("1. Bubble Sort")
    print("2. Merge Sort")
    print("3. Selection Sort")
    print("4. Insertion Sort")
    choice = int(input("Your choice: "))

    sorted_arr = switch_case(choice, arr.copy())
    
    if isinstance(sorted_arr, list):
        print(f"Sorted array: {sorted_arr}")
    else:
        print(sorted_arr)
        