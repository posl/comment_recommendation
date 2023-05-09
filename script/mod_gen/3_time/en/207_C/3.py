def main():
    N = int(input())
    T, L, R = [], [], []
    for _ in range(N):
        t, l, r = map(int, input().split())
        T.append(t)
        L.append(l)
        R.append(r)
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if T[i] == 1:
                if T[j] == 1:
                    if L[i] <= L[j] <= R[i] or L[i] <= R[j] <= R[i]:
                        ans += 1
                elif T[j] == 2:
                    if L[i] <= L[j] <= R[i] or L[i] <= R[j] < R[i]:
                        ans += 1
                elif T[j] == 3:
                    if L[i] < L[j] <= R[i] or L[i] < R[j] < R[i]:
                        ans += 1
                else:
                    if L[i] < L[j] <= R[i] or L[i] < R[j] < R[i]:
                        ans += 1
            elif T[i] == 2:
                if T[j] == 1:
                    if L[i] <= L[j] <= R[i] or L[i] < R[j] <= R[i]:
                        ans += 1
                elif T[j] == 2:
                    if L[i] <= L[j] <= R[i] or L[i] < R[j] <= R[i]:
                        ans += 1
                elif T[j] == 3:
                    if L[i] < L[j] <= R[i] or L[i] < R[j] <= R[i]:
                        ans += 1
                else:
                    if L[i] < L[j] <= R[i] or L[i] < R[j] <= R[i]:
                        ans += 1
            elif T[i] == 3:
                if T[j] == 1:
                    if L[i] <= L[j] < R[i] or L[i] <= R[j] < R[i]:
                        ans += 1
                elif T[j] == 2:
                    if L[i] <= L[j] < R[i] or L[i] < R[j] < R[i]:
                        ans += 1
                elif T

if __name__ == '__main__':
    main()