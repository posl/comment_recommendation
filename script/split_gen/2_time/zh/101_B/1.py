def f(n):
    return sum(map(int, str(n)))
n = int(input())
print('Yes' if n % f(n) == 0 else 'No')
