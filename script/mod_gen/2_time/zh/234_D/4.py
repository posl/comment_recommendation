def findKthNumber(k):
    if k <= 0:
        return 0
    if k <= 2:
        return k*10
    k -= 2
    n = 1
    while k > 0:
        if k >= 2**n:
            k -= 2**n
            n += 1
        else:
            k -= 1
            n -= 1
    ans = 2
    for i in range(n-1):
        ans = ans*10+2
    return ans

if __name__ == '__main__':
    findKthNumber()