def resize_array(arr, new_size):
    if new_size < len(arr):
        return arr[:new_size]  # Truncate the array if new size is smaller
    else:
        return arr + [0] * (new_size - len(arr))  # Pad the array with zeros if new size is larger

# Example usage:
original_array = [1, 2, 3, 4, 5]
new_size = 8
resized_array = resize_array(original_array, new_size)
print(len(resized_array))


