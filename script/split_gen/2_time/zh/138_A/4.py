def solve():
    N, M = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0])
    # print(AB)
    ans = 0
    for i in range(N):
        if M >= AB[i][0]:
            ans += AB[i][1]
            M -= 1
    print(ans)
