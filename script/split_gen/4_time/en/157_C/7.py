def main():
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]
    ans = [-1 for _ in range(n)]
    for s, c in sc:
        if ans[s-1] == -1 or ans[s-1] == c:
            ans[s-1] = c
        else:
            print(-1)
            return
    if ans[0] == 0 and n > 1:
        print(-1)
        return
    if ans[0] == -1:
        ans[0] = 1
    print(''.join(map(str, ans)))
