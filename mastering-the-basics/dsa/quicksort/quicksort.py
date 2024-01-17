# Quicksort Implementation
# Features:
    # One of the fastest sorting algorithms
# Time Complexity: Worst: O(n^2) Average: O(nlogn)
# Space Complexity: Worst: O(n) Average: O(nlogn)

def quicksort(list):
    # Base cases
    if len(list) < 2:
        return list
    
    # Recursive Case
    pivot = 0
    frontier = pivot + 1

    for i in range(1, len(list)):
        if list[i] <= list[pivot]:
            list[frontier], list[i] = list[i], list[frontier]
            frontier += 1


    list[frontier - 1], list[pivot] = list[pivot], list[frontier - 1]
    pivot = frontier - 1

    return quicksort(list[0 : pivot]) + [list[pivot]] + quicksort(list[pivot + 1 : len(list)])


if __name__ == "__main__":
    # Test 1: List is empty
    list = []
    expected = []
    result = quicksort(list)
    print(f'Test 1: {"Passed" if result == expected else "Failed"}')

    # Test 2: General case
    list = [2, 4, 5, 1]
    expected = [1, 2, 4, 5]
    result = quicksort(list)
    print(f'Test 2: {"Passed" if result == expected else "Failed"}')
    
    # Test 3: 2 Elements unsorted
    list = [4, 2]
    expected = [2, 4]
    result = quicksort(list)
    print(f'Test 3: {"Passed" if result == expected else "Failed"}')




        