def main():
    S = input()
    N = len(S)
    count = [0] * N
    count[0] = 1
    count[-1] = 1
    for i in range(1, N - 1):
        if S[i] == 'R':
            count[i] = count[i - 1] + 1
        else:
            count[i] = count[i - 1] - 1
    for i in range(N - 2, 0, -1):
        if S[i] == 'L':
            count[i] = count[i + 1] + 1
        else:
            count[i] = count[i + 1] - 1
    print(*count)

if __name__ == '__main__':
    main()