def main():
    N, K = map(int, input().split())
    S = input()
    count = 0
    for i in range(1, N):
        if S[i] == S[i-1]:
            count += 1
    count += 2 * K
    print(min(count, N-1))

if __name__ == '__main__':
    main()