def calc(n):
    if n < 12:
        return 0
    elif n == 12:
        return 1
    else:
        return calc(n-1) + calc(n-2) + calc(n-3) + calc(n-4) + calc(n-5) + calc(n-6) + calc(n-7) + calc(n-8) + calc(n-9) + calc(n-10) + calc(n-11) + calc(n-12)
n = int(input())
print(calc(n))
