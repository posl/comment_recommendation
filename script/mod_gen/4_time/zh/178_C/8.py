def f(n):
    return 10**n - 9**n - 9**n + 8**n
n = int(input())
print(f(n) % (10**9 + 7))
