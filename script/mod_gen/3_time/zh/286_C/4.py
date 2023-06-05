def main():
    N, A, B = map(int, input().split())
    S = input()
    cnt = 0
    cnt_b = 0
    for i in range(N):
        if S[i] != S[N - i - 1]:
            if S[i] == 'a' or S[N - i - 1] == 'a':
                cnt_b += 1
            else:
                print(-1)
                return
        elif S[i] == 'a':
            cnt += 1
    if cnt_b == 0:
        print(0)
        return
    if cnt == N:
        print(A * N + B * (N - 1))
        return
    if S[N // 2] == 'a':
        print(A * N + B * cnt_b)
    else:
        print(A * N + B * (cnt_b - 1))

if __name__ == '__main__':
    main()