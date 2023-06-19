def main():
    n = int(input())
    L = []
    R = []
    for i in range(n):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    print(L[0],R[-1])
    return 0
