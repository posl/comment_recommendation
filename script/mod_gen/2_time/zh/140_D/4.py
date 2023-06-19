def main():
    N, K = map(int, input().split())
    S = input()
    cnt = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            cnt += 1
    cnt += 2 * K
    if cnt > N-1:
        cnt = N-1
    print(cnt)

if __name__ == '__main__':
    main()