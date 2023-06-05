def S(n):
    return sum(map(int, str(n)))
n = int(input())
print('Yes' if n % S(n) == 0 else 'No')
