def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle 
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


numbers = [2, 4, 6, 8, 10, 12, 14, 16]
search_value = 10

result = binary_search(numbers, search_value)

if result != -1:
    print(f"Element {search_value} znaleziony na indeksie {result}.")
else:
    print(f"Element {search_value} nie został znaleziony w tablicy.")
