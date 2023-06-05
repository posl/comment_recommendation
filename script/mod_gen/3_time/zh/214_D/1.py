def main():
    n = int(input())
    w = [0] * (n + 1)
    for _ in range(n - 1):
        u, v, w_ = map(int, input().split())
        w[u] += w_
        w[v] += w_
    ans = sum(w[i] * w[j] for i in range(1, n + 1) for j in range(i + 1, n + 1))
    print(ans)

if __name__ == '__main__':
    main()