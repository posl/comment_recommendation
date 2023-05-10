def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(m):
        a, b = map(int, input().split())
        ab.append([a, b])
    ab.sort()
    ans = 0
    for i in range(m):
        if ab[i][1] in ab[i + 1:]:
            ans += 1
    print(ans)
