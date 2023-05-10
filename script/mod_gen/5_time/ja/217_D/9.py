def main():
    L, Q = map(int, input().split())
    q = [list(map(int, input().split())) for _ in range(Q)]
    q = [[c, x] for c, x in q if c == 1]
    q.sort(key=lambda x: x[1])
    ans = [0] * Q
    ans[0] = L
    for i in range(1, len(q)):
        ans[i] = q[i][1] - q[i - 1][1]
    ans[-1] = L - q[-1][1]
    for i in range(Q):
        if q[i][0] == 2:
            print(ans[i])

if __name__ == '__main__':
    main()