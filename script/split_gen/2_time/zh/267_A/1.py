def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t,x,a = map(int,input().split())
        snuke.append([t,x,a])
    snuke.sort()
    ans = 0
    for i in range(n):
        if snuke[i][1] == 0:
            ans += snuke[i][2]
            snuke[i][2] = 0
    for i in range(n):
        if snuke[i][1] == 4:
            ans += snuke[i][2]
            snuke[i][2] = 0
    for i in range(n):
        if snuke[i][1] == 1:
            if snuke[i][2] > snuke[i+1][2]:
                ans += snuke[i][2]
                snuke[i][2] = 0
            else:
                ans += snuke[i+1][2]
                snuke[i+1][2] = 0
        if snuke[i][1] == 3:
            if snuke[i][2] > snuke[i+1][2]:
                ans += snuke[i][2]
                snuke[i][2] = 0
            else:
                ans += snuke[i+1][2]
                snuke[i+1][2] = 0
    print(ans)
main()
