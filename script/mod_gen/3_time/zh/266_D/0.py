def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t,x,a = map(int,input().split())
        snuke.append([t,x,a])
    ans = 0
    for i in range(1,n):
        if snuke[i][0] - snuke[i-1][0] >= abs(snuke[i][1] - snuke[i-1][1]):
            ans += snuke[i][2]
    print(ans)
main()
