def main():
    N = int(input())
    S = [0] * (N + 1)
    S[0] = 1
    for i in range(1, N + 1):
        S[i] = S[i - 1]
        if i % 3 == 0:
            S[i] += S[i // 3]
        if i % 5 == 0:
            S[i] += S[i // 5]
        if i % 7 == 0:
            S[i] += S[i // 7]
    print(S[N])
main()
