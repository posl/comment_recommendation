def main():
    N = int(input())
    S = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(1, S[i] + 1):
            if (4 * j * (S[i] - j) + 3 * j + 3 * (S[i] - j)) == S[i]:
                break
            elif j == S[i]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()