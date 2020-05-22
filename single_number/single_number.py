'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # Set up inner and outer loop to stay in one pass
    for i in range(len(arr)):
        # set condition to find duplicates
        dupe = False
        for n in range(len(arr)):
            # Inner loop to check if the current number matches any other numbers in array
            if i != n and arr[i] == arr[n]:
                # if dupe is found, set condition to loop
                dupe = True
        # If dupe isn't found, exit loop
        if not dupe:
            return arr[i]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")