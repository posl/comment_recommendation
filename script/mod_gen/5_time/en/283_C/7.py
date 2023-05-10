def main():
    S = input()
    N = len(S)
    ans = N
    for i in range(2**N):
        cnt = 0
        tmp = 0
        for j in range(N):
            if i & (1 << j):
                cnt += 1
                tmp = 0
            tmp = tmp * 10 + int(S[j])
        cnt += len(str(tmp))
        ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()