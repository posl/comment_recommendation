def solve():
    N, M = map(int, input().split())
    works = []
    for i in range(N):
        works.append(list(map(int, input().split())))
    works.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while M > 0:
        if works[i][0] > M:
            break
        else:
            ans += works[i][1]
            M -= works[i][0]
            i += 1
    print(ans)
