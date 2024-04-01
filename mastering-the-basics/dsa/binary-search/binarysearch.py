# Binary Search Implementation
# Features: 
    # Must be given a sorted list

# Time Complexity: O(log n)
# Space Complexity: O(1)

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2

        if list[mid] == item:
            return mid
        elif list[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return None




if __name__ == "__main__":

    # Test 1: List is empty
    list = []
    expected = None
    result = binary_search(list, 1)
    print(f'Test 1: {"Passed" if result == expected else "Failed"}')

    # Test 2: General case
    list = [2, 4, 5, 1]
    expected = 2
    result = binary_search(list, 5)
    print(f'Test 2: {"Passed" if result == expected else "Failed"}')