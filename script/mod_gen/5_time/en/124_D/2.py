def main():
    N, K = map(int, input().split())
    S = input()
    count = 0
    if S[0] == '0':
        count += 1
    for i in range(1, N):
        if S[i] == '1' and S[i - 1] == '0':
            count += 1
    print(min(N, count + 2 * K))

if __name__ == '__main__':
    main()