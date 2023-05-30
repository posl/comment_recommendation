def check(n):
    for i in range(0, n+1):
        for j in range(0, n+1):
            if 4*i + 7*j == n:
                return True
    return False
n = int(input())
print('Yes' if check(n) else 'No')
