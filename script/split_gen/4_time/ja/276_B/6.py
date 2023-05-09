def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort()
    ans = [[] for _ in range(n)]
    for a, b in ab:
        ans[a-1].append(b)
        ans[b-1].append(a)
    for i in range(n):
        print(len(ans[i]), *ans[i])
