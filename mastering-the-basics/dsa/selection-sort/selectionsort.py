# Inplace Selection Sort Implementation
# Features:
    # Simple sorting implementation
# Time Complexity: O(n^2)
# Space Complexity: O(1)

        
def selection_sort(list) -> list:

    for i in range(len(list)):
        smallest = i
        # Find index of smallest value in sublist
        for j in range(i, len(list)):
            if list[j] < list[smallest]:
                smallest = j
        
        # Swap with value at i
        if smallest != i:
            list[smallest], list[i] = list[i], list[smallest]
    return list

if __name__ == "__main__":
    # Test 1: General case
    list = [2, 4, 1, 6]
    expected = [1, 2, 4, 6]
    result = selection_sort(list)
    print(f'Test 1: {"Passed" if result == expected else "Failed"}')

    # Test 2: Empty list
    list = []
    expected = []
    result = selection_sort(list)
    print(f'Test 2: {"Passed" if result == expected else "Failed"}')

    # Test 3: Single item
    list = [1]
    expected = [1]
    result = selection_sort(list)
    print(f'Test 3: {"Passed" if result == expected else "Failed"}')