def main():
    N, K = map(int, input().split())
    S = input().rstrip()
    ans = 0
    cnt = 0
    for i in range(N):
        if S[i] == "0":
            cnt += 1
        else:
            if K > 0:
                K -= 1
            else:
                while S[i] == "1":
                    i += 1
                i -= 1
                ans = max(ans, cnt)
                cnt = 0
    ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()