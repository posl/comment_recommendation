def main():
    N, Q = map(int, input().split())
    next = [i + 1 for i in range(N)]
    prev = [i - 1 for i in range(N)]
    for _ in range(Q):
        c, x, y = map(int, input().split())
        if c == 1:
            prev[next[x - 1]] = y - 1
            next[prev[y - 1]] = x - 1
            prev[x - 1] = y - 1
            next[y - 1] = x - 1
        elif c == 2:
            prev[next[x - 1]] = prev[y - 1]
            next[prev[y - 1]] = next[x - 1]
            prev[x - 1] = x - 1
            next[y - 1] = y - 1
        else:
            ans = []
            while x > 0:
                ans.append(x)
                x = next[x - 1] + 1
            print(len(ans), *ans)
