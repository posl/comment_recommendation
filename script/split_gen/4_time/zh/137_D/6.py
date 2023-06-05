def main():
    n,m = map(int,input().split())
    ab = []
    for i in range(n):
        ab.append(list(map(int,input().split())))
    ab.sort(key=lambda x:x[0])
    ans = 0
    for i in range(n):
        if m == 0:
            break
        if m >= ab[i][0]:
            m -= ab[i][0]
            ans += ab[i][1]
    print(ans)
