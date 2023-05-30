def problems214_a(n):
    if n < 126:
        return 4
    elif n < 212:
        return 6
    else:
        return 8
n = int(input())
print(problems214_a(n))
