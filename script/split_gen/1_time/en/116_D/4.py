def main():
    N, K = map(int, input().split())
    Sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        Sushi.append((t, d))
    Sushi.sort(key=lambda x: x[1], reverse=True)
    Sushi = Sushi[:K]
    Sushi.sort(key=lambda x: x[0])
    kind = {}
    for i in range(K):
        if Sushi[i][0] in kind:
            kind[Sushi[i][0]] += 1
        else:
            kind[Sushi[i][0]] = 1
    kind = list(kind.values())
    kind.sort()
    ans = 0
    for i in range(len(kind)):
        ans += kind[i] * kind[i]
    ans += sum([Sushi[i][1] for i in range(len(kind))])
    for i in range(len(kind)):
        tmp = ans
        tmp -= kind[i] * kind[i]
        tmp += (kind[i] + 1) * (kind[i] + 1)
        tmp -= sum([Sushi[j][1] for j in range(kind[i])])
        tmp += sum([Sushi[j][1] for j in range(kind[i], len(kind))])
        ans = max(ans, tmp)
    print(ans)
