def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N):
        for j in range(i+1,N+1):
            if int(S[i:j]) % 2019 == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()