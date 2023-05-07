def main():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    ans = []
    l = L[0]
    r = R[0]
    for i in range(N-1):
        if l <= L[i+1] and R[i+1] <= r:
            continue
        elif l <= L[i+1] and L[i+1] <= r:
            r = R[i+1]
        else:
            ans.append([l,r])
            l = L[i+1]
            r = R[i+1]
    ans.append([l,r])
    for a in ans:
        print(*a)
