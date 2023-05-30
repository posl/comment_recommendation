def main():
    n,m = map(int,input().split())
    days = []
    for i in range(n):
        a,b = map(int,input().split())
        days.append((a,b))
    days.sort()
    ans = 0
    for i in range(n):
        if m == 0:
            break
        if days[i][0] <= m:
            m -= days[i][0]
            ans += days[i][1]
        else:
            ans += m * days[i][1]
            m = 0
    print(ans)
main()
