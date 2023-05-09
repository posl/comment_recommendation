def main():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    i = 0
    j = 0
    ans = []
    while i < N and j < N:
        if L[i] <= R[j]:
            l = L[i]
            i += 1
            while i < N and L[i] <= R[j]:
                i += 1
            r = R[j]
            j += 1
            while j < N and L[i-1] <= R[j]:
                j += 1
            ans.append([l,r])
    print(*ans, sep='
')

if __name__ == '__main__':
    main()