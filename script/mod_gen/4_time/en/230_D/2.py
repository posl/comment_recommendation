def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    #print(L)
    #print(R)
    i = 0
    j = 0
    ans = 0
    while i < N:
        while j < N and R[j] < L[i] + D:
            j += 1
        ans += 1
        i = j
    print(ans)

if __name__ == '__main__':
    main()