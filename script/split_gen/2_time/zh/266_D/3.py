def solve():
    n = int(input())
    snuke = []
    for i in range(n):
        snuke.append(list(map(int, input().split())))
    for i in range(n):
        snuke[i][2] += snuke[i][0]
    snuke.sort(key=lambda x:x[2])
    ans = 0
    for i in range(n):
        if i == 0:
            if snuke[i][1] == 0:
                ans += snuke[i][2]
        else:
            if snuke[i][1] == snuke[i-1][1]:
                if snuke[i][2] > snuke[i-1][2]:
                    ans += snuke[i][2] - snuke[i-1][2]
            else:
                if snuke[i][1] - snuke[i-1][1] == 1:
                    ans += snuke[i][2] - snuke[i-1][2]
                elif snuke[i][1] - snuke[i-1][1] == 2:
                    if snuke[i][2] > snuke[i-1][2]:
                        ans += snuke[i][2] - snuke[i-1][2]
                elif snuke[i][1] - snuke[i-1][1] == 3:
                    if snuke[i][2] > snuke[i-1][2]:
                        ans += snuke[i][2] - snuke[i-1][2]
                elif snuke[i][1] - snuke[i-1][1] == 4:
                    if snuke[i][2] > snuke[i-1][2]:
                        ans += snuke[i][2] - snuke[i-1][2]
                else:
                    pass
    print(ans)
solve()
