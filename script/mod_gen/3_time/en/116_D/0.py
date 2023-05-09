def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    t_set = set()
    d_sum = 0
    for i in range(K):
        t, d = sushi[i]
        t_set.add(t)
        d_sum += d
        ans = max(ans, d_sum + len(t_set)**2)
    for i in range(K, N):
        t, d = sushi[i]
        if t in t_set:
            continue
        t_set.add(t)
        d_sum += d
        d_sum -= sushi[K-1][1]
        K -= 1
        ans = max(ans, d_sum + len(t_set)**2)
    print(ans)
main()
The following code is the solution for the problem "D - Grid Components" on AtCoder.

if __name__ == '__main__':
    main()