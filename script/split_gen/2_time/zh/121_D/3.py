def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort()
    ans = 0
    for i in range(n):
        if ab[i][1] >= m:
            ans += ab[i][0] * m
            break
        else:
            ans += ab[i][0] * ab[i][1]
            m -= ab[i][1]
    print(ans)
