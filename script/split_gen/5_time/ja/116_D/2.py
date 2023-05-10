def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append([d, t])
    sushi.sort(reverse=True)
    eat = []
    eat_kind = []
    ans = 0
    for i in range(N):
        if i < K:
            ans += sushi[i][0]
            if sushi[i][1] not in eat_kind:
                eat_kind.append(sushi[i][1])
            else:
                eat.append(sushi[i][0])
        else:
            if sushi[i][1] not in eat_kind:
                eat.append(sushi[i][0])
    eat.sort(reverse=True)
    eat_kind.sort()
    ans += sum(eat_kind)**2
    ans += sum(eat)
    print(ans)
