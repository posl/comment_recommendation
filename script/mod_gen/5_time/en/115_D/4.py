def count_patty(n, x):
    if x == 1:
        return 0
    elif x <= 2**(n+1) - 3:
        return count_patty(n-1, x-1)
    else:
        return 2**n + count_patty(n-1, x - 2**(n+1) + 2)
n, x = map(int, input().split())
print(count_patty(n, x))
