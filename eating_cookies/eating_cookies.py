'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, mem=None):
    # Your code here
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif mem and mem[n] > 0:
        return mem[n]
    else:
        if not mem:
            mem = [0 for _ in range(n+1)]
        mem[n] = eating_cookies(n-1, mem) + eating_cookies(n-2, mem) + eating_cookies(n-3, mem)
    return mem[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
