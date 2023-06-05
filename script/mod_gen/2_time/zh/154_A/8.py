def calc(n):
    if n == 1:
        return 1
    else:
        return 2 * calc(n//2) + 1
H = int(input())
print(calc(H))
