'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    for i in range(len(arr)):
        check = 0
        for n in range(len(arr)):
            if arr[i] == check:
                arr.append(arr[i])
                del arr[i]
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 2, 3, 0, 4, 0, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")