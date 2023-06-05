def solve():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    #print(AB)
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            ans += AB[i][0]
        else:
            ans -= AB[i][1]
    print(ans)
