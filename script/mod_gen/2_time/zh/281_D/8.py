def findMaxSum(n, k, d, a):
    # Write your code here
    if k == 1:
        if a[0] % d == 0:
            return -1
        else:
            return a[0]
    elif k == 2:
        if a[0] % d == 0 and a[1] % d == 0:
            return -1
        else:
            return a[0] + a[1]
    else:
        if a[0] % d == 0 and a[1] % d == 0:
            return -1
        else:
            return a[0] + a[1] + a[2]

if __name__ == '__main__':
    findMaxSum()