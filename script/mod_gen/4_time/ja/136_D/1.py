def main():
    S = input()
    N = len(S)
    L = []
    R = []
    for i in range(N):
        if S[i] == 'L':
            L.append(i)
        else:
            R.append(i)
    ans = [0] * N
    for i in R:
        if (i - L[0]) % 2 == 0:
            ans[L[0]] += 1
        else:
            ans[L[0] - 1] += 1
    for i in L:
        if (R[-1] - i) % 2 == 0:
            ans[R[-1]] += 1
        else:
            ans[R[-1] + 1] += 1
    for i in range(len(L) - 1):
        if (L[i + 1] - L[i]) % 2 == 0:
            ans[L[i + 1]] += 1
        else:
            ans[L[i + 1] - 1] += 1
    for i in range(len(R) - 1):
        if (R[i + 1] - R[i]) % 2 == 0:
            ans[R[i + 1]] += 1
        else:
            ans[R[i + 1] + 1] += 1
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()