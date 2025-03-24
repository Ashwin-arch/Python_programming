def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found

    return -1  # Return -1 if the target is not found

# Example usage
my_list = [3, 7, 1, 9, 4, 2, 6]
target_element = 4

result = linear_search(my_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
