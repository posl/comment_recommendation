def main():
    S = input()
    N = len(S)
    cnt = 0
    for i in range(N):
        for j in range(i+1,N+1):
            if int(S[i:j]) % 2019 == 0:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()