def main():
    N, Q = map(int, input().split())
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
    tree[1].append(1)
    point = [0] * (N+1)
    for _ in range(Q):
        p, x = map(int, input().split())
        point[p] += x
    ans = [0] * (N+1)
    ans[1] = point[1]
    for i in range(2, N+1):
        ans[i] = ans[i-1] + point[i]
    for i in range(1, N+1):
        print(ans[i], end=" ")

if __name__ == '__main__':
    main()