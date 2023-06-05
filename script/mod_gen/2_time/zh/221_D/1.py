def solve():
    N = int(input())
    digits = []
    while N > 0:
        digits.append(N % 10)
        N //= 10
    digits.sort(reverse=True)
    a = []
    b = []
    for i in range(len(digits)):
        if i % 2 == 0:
            a.append(digits[i])
        else:
            b.append(digits[i])
    a = int("".join(map(str, a)))
    b = int("".join(map(str, b)))
    print(a * b)
solve()
