def main():
    N, Q = map(int, input().split())
    par = [-1] * (N + 1)
    rank = [0] * (N + 1)
    for _ in range(Q):
        query = list(map(int, input().split()))
        c = query[0]
        if c == 1:
            x, y = query[1], query[2]
            unite(x, y, par, rank)
        elif c == 2:
            x, y = query[1], query[2]
            if same(x, y, par):
                unite(x, y, par, rank)
        else:
            x = query[1]
            ans = []
            for i in range(1, N + 1):
                if same(x, i, par):
                    ans.append(i)
            print(len(ans), *ans)
