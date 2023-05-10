def main():
    n, k = map(int, input().split())
    sushi = []
    for i in range(n):
        sushi.append(list(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    used = []
    ans = 0
    for i in range(k):
        t, d = sushi.pop()
        ans += d
        if t not in used:
            used.append(t)
    ans += len(used) ** 2
    while len(used) < k and len(sushi) > 0:
        t, d = sushi.pop()
        if t not in used:
            ans += d
            used.append(t)
    print(ans)
