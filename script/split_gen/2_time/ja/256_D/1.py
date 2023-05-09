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
    for i in range(N):
        if L[i] < R[i]:
            ans.append([L[i], R[i]])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
