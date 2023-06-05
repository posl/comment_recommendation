def S(n):
    if n==1:
        return [1]
    else:
        x = S(n-1)
        return x + [n] + x
n = int(input())
print(" ".join(map(str, S(n))))
