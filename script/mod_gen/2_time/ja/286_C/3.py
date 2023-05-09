def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    if A < B:
        cnt = 1
        for i in range(1, N):
            if S[i] != S[i-1]:
                if S[i-1] == "a":
                    ans += A
                else:
                    ans += B
                cnt = 1
            else:
                cnt += 1
        if cnt % 2 == 1:
            ans += A
    else:
        ans = A * N
    print(ans)

if __name__ == '__main__':
    main()