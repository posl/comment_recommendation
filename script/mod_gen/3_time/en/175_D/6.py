def main():
    N, K = map(int, input().split())
    P = list(map(lambda x: int(x)-1, input().split()))
    C = list(map(int, input().split()))
    ans = -10**9
    for start in range(N):
        now = start
        score = 0
        loop = 0
        while True:
            score += C[now]
            now = P[now]
            loop += 1
            if now == start:
                break
        if score > 0:
            loop = min(loop, K)
            num = K // loop
            rem = K % loop
            ans = max(ans, score * num + sum(C[P[i]] for i in range(rem)))
        else:
            ans = max(ans, sum(C[P[i]] for i in range(min(loop, K))))
    print(ans)

if __name__ == '__main__':
    main()