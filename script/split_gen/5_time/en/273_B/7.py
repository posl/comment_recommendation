def roundoff(x, k):
    for i in range(k):
        if x%10 == 0:
            x = x/10
        else:
            x = x - x%10 + 10
    return int(x)
x, k = map(int, input().split())
print(roundoff(x, k))
