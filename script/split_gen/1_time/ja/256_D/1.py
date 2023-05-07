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
    for i in range(N):
        if L[i] != R[i]:
            print(L[i], R[i])
            return
