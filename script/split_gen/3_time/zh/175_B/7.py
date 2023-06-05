def isTriangle(a, b, c):
    return a < b + c and b < c + a and c < a + b
n = int(input())
sticks = list(map(int, input().split()))
sticks.sort()
count = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if isTriangle(sticks[i], sticks[j], sticks[k]):
                count += 1
print(count)
