def calc(n):
    if n == 0:
        return 0
    elif n < 6:
        return 1
    elif n < 9:
        return 2
    else:
        return 1 + min(calc(n - 6**i) for i in range(1, 10) if n >= 6**i) + min(calc(n - 9**i) for i in range(1, 10) if n >= 9**i)
N = int(input())
print(calc(N))

if __name__ == '__main__':
    calc()