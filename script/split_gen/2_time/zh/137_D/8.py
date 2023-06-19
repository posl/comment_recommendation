def main():
    n,m = map(int,input().split())
    ab = []
    for i in range(n):
        ab.append(list(map(int,input().split())))
    ab.sort(key=lambda x:x[0])
    ab.sort(key=lambda x:x[1],reverse=True)
    print(ab)
    ans = 0
    for i in range(n):
        if m >= ab[i][0]:
            ans += ab[i][1]
            m -= ab[i][0]
        else:
            ans += m * ab[i][1]
            break
    print(ans)
