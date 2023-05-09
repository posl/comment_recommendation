def main():
    N, K = map(int, input().split())
    T = []
    for _ in range(N):
        t, d = map(int, input().split())
        T.append((t, d))
    T.sort(key=lambda x: x[1], reverse=True)
    T = T[:K]
    T.sort()
    t = [0] * (N + 1)
    for i in range(K):
        t[T[i][0]] += 1
    ans = 0
    for i in range(K):
        ans += T[i][1]
    ans += t.count(1) * t.count(1)
    tmp = ans
    for i in range(K):
        if t[T[i][0]] == 1:
            continue
        t[T[i][0]] -= 1
        tmp -= T[i][1]
        tmp -= t.count(1) * t.count(1)
        tmp += t.count(1) * t.count(1)
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()