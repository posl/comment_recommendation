def main():
    n,m = map(int,input().split())
    ab = []
    for i in range(n):
        ab.append(list(map(int,input().split())))
    ab.sort(key=lambda x:x[0])
    count = 0
    ans = 0
    for i in range(n):
        if count + ab[i][1] < m:
            ans += ab[i][0] * ab[i][1]
            count += ab[i][1]
        else:
            ans += ab[i][0] * (m - count)
            break
    print(ans)
