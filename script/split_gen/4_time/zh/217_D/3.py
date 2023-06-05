def main():
    L, Q = map(int, input().split())
    mark = [0] * (L + 1)
    mark[1] = L
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            mark[x] = x
        else:
            ans = mark[x]
            for j in range(x, 0, -1):
                if mark[j] != 0:
                    ans = mark[j]
                    break
            print(ans)
