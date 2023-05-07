def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append([t, d])
    sushi.sort(key=lambda x: x[1], reverse=True)
    #print(sushi)
    ans = 0
    t = set()
    s = 0
    for i in range(K):
        s += sushi[i][1]
        t.add(sushi[i][0])
        ans = max(ans, s + len(t) ** 2)
    #print(s, len(t), ans)
    for i in range(K, N):
        if sushi[i][0] in t:
            continue
        t.add(sushi[i][0])
        t.remove(sushi[i - len(t) + 1][0])
        s += sushi[i][1] - sushi[i - len(t) + 1][1]
        ans = max(ans, s + len(t) ** 2)
    print(ans)
