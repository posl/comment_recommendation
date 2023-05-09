def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    W1 = []
    W2 = []
    for i in range(N):
        if S[i] == "0":
            W1.append(W[i])
        else:
            W2.append(W[i])
    W1.sort()
    W2.sort()
    ans = 0
    for i in range(N):
        if S[i] == "0":
            idx = bisect_left(W2, W[i])
            ans = max(ans, idx + N - i - 1)
        else:
            idx = bisect_right(W1, W[i])
            ans = max(ans, i - idx + 1)
    print(ans)

if __name__ == '__main__':
    main()