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
    ans = []
    for i in range(N - 1):
        if R[i] < L[i + 1]:
            ans.append([L[i], R[i]])
            L[i + 1] = L[i]
    ans.append([L[N - 1], R[N - 1]])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
main()
