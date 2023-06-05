def main():
    S = input()
    N = len(S)
    cnt = 0
    for i in range(N):
        if (i % 2 == 0 and S[i] == '1') or (i % 2 == 1 and S[i] == '0'):
            cnt += 1
    print(min(cnt, N - cnt))

if __name__ == '__main__':
    main()