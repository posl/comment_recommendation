def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1] * N
    for i in range(N):
        P[i] -= 1
    for i in range(N):
        if ans[i] == -1:
            move = 1
            cur = P[i]
            while ans[cur] == -1:
                ans[cur] = move
                move += 1
                cur = P[cur]
            for j in range(N):
                if ans[j] != -1:
                    ans[j] = (ans[j] - 1) % (move - 1) + 1
    for i in range(N):
        if ans[i] > K:
            ans[i] = -1
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()