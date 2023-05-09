def main():
    N = int(input())
    T = [0] * N
    L = [0] * N
    R = [0] * N
    ans = 0
    for i in range(N):
        T[i], L[i], R[i] = map(int, input().split())
        if T[i] == 1:
            L[i] *= 2
            R[i] = R[i] * 2 - 1
        elif T[i] == 2:
            L[i] *= 2
            R[i] = R[i] * 2 - 2
        elif T[i] == 3:
            L[i] = L[i] * 2 + 1
            R[i] = R[i] * 2
        else:
            L[i] = L[i] * 2 + 2
            R[i] = R[i] * 2
    for i in range(N):
        for j in range(i + 1, N):
            if max(L[i], L[j]) <= min(R[i], R[j]):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()