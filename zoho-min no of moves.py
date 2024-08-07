def move_even_odd(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        # Increment left index while we see even number at left
        while arr[left] % 2 == 0 and left < right:
            left += 1

        # Decrement right index while we see odd number at right
        while arr[right] % 2 == 1 and left < right:
            right -= 1

        if left < right:
            # Swap arr[left] and arr[right]
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

def print_array(arr):
    for num in arr:
        print(num, end=' ')
    print()

if __name__ == "__main__":
    arr = [111, 222, 333,444,555,666,777,888,999,1000]

    print("Original array:")
    print_array(arr)

    move_even_odd(arr)

    print("Array after segregation:")
    print_array(arr)
