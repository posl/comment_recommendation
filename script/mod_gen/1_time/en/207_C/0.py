def main():
    N = int(input())
    T = []
    L = []
    R = []
    for i in range(N):
        t, l, r = map(int, input().split())
        T.append(t)
        L.append(l)
        R.append(r)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if T[i] == 1:
                if T[j] == 1:
                    if L[i] <= R[j] and L[j] <= R[i]:
                        ans += 1
                elif T[j] == 2:
                    if L[i] < R[j] and L[j] <= R[i]:
                        ans += 1
                elif T[j] == 3:
                    if L[i] <= R[j] and L[j] < R[i]:
                        ans += 1
                elif T[j] == 4:
                    if L[i] < R[j] and L[j] < R[i]:
                        ans += 1
            elif T[i] == 2:
                if T[j] == 1:
                    if L[i] <= R[j] and L[j] < R[i]:
                        ans += 1
                elif T[j] == 2:
                    if L[i] < R[j] and L[j] < R[i]:
                        ans += 1
                elif T[j] == 3:
                    if L[i] <= R[j] and L[j] <= R[i]:
                        ans += 1
                elif T[j] == 4:
                    if L[i] < R[j] and L[j] <= R[i]:
                        ans += 1
            elif T[i] == 3:
                if T[j] == 1:
                    if L[i] < R[j] and L[j] <= R[i]:
                        ans += 1
                elif T[j] == 2:
                    if L[i] <= R[j] and L[j] < R[i]:
                        ans += 1
                elif T[j] == 3:
                    if L[i] < R[j] and L[j] < R[i]:
                        ans += 1
                elif T[j] == 4:
                    if L[i] <= R[j] and L[j] < R[i]:
                        ans += 1
            elif T[i] == 4:

if __name__ == '__main__':
    main()