def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**18
    for i in range(N):
        score = 0
        loop = []
        j = i
        while True:
            score += C[j]
            j = P[j] - 1
            if j in loop:
                break
            loop.append(j)
        if score <= 0:
            ans = max(ans, max(C))
        else:
            cnt = 0
            for j in loop:
                cnt += 1
                if j == i:
                    break
            ans = max(ans, max(C) * (K // cnt) + max(C[:K % cnt + 1]))
    print(ans)
main()

if __name__ == '__main__':
    main()