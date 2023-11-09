def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

# Taking input from the user
n = int(input("Enter the number of elements: "))
input_list = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    input_list.append(num)

print("Unsorted list:", input_list)

selection_sort(input_list)

print("Sorted list using Selection Sort:", input_list)
