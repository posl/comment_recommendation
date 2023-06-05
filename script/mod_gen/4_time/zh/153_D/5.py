def f(n):
    if n == 1:
        return 1
    else:
        return 2*f(n//2)+1
H = int(input())
print(f(H))
