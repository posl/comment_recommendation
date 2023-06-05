def solve():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    sumA = sum([a for a, b in AB])
    sumB = 0
    ans = 0
    for a, b in AB:
        sumA -= a
        sumB += a + b
        ans += 1
        if sumB > sumA:
            break
    print(ans)
