def countFlowers(n, a, b):
    count = 0
    for i in range(1, n+1):
        if i != a and i != b:
            count += 1
    return count
n, a, b = map(int, input().split())
print(countFlowers(n, a, b))
