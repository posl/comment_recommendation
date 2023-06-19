def sequence(n):
    if n == 1:
        return [1]
    else:
        return sequence(n-1) + [n] + sequence(n-1)
n = int(input())
print(*sequence(n))
