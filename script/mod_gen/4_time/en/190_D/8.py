def arithmetic_progression(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        for i in range(1, n):
            if n == i * (i + 1) // 2:
                return i + 1
            elif n < i * (i + 1) // 2:
                return i
print(arithmetic_progression(int(input())))
