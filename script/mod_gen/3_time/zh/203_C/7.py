def main():
    N, K = map(int, input().split())
    A_B = [list(map(int, input().split())) for _ in range(N)]
    A_B.sort()
    now = 0
    for i in range(N):
        if A_B[i][0] - now <= K:
            K -= A_B[i][0] - now
            K += A_B[i][1]
            now = A_B[i][0]
        else:
            now += K
            break
    print(now + K)
main()
