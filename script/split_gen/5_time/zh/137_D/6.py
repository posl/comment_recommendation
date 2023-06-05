def main():
    n, m = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    i = 0
    ans = 0
    for _ in range(m):
        while i < n and ab[i][0] <= _ + 1:
            ans = max(ans, ab[i][1])
            i += 1
        print(ans)
