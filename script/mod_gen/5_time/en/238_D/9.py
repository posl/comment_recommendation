def isPowerOfTwo(n):
    if n==0:
        return False
    return n & (n-1) == 0

if __name__ == '__main__':
    isPowerOfTwo()