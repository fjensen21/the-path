# Basic recursion problems
# Divide and Conquer:
    # 1. Figure out the base case (simplest case)
    # 2. Divide or decrease your problem until it becomes the base case

def recursive_sum(list):
    # Base Case
    if len(list) == 0:
        return 0
    
    # Recursive Case
    return list[0] + recursive_sum(list[1:len(list)])

def max_num(list):
    # Base Case
    if len(list) == 0:
        return None
    if len(list) == 1:
        return list[0]
    
    # Recursive
    greatest = max_num(list[1 : len(list)])
    if list[0] > greatest:
        return list[0]
    else:
        return greatest

if __name__ == "__main__":
    print(f'Expected: 6\nActual: {recursive_sum([1, 2, 3])}')
    print(f'Expected: 7\nActual: {max_num([1,2,7])}')