def main():
    n = int(input())
    L = [0]*n
    R = [0]*n
    for i in range(n):
        L[i],R[i] = map(int,input().split())
    L.sort()
    R.sort()
    for i in range(n-1):
        if R[i] < L[i+1]:
            print(L[i],R[i])
            print(L[i+1],R[i+1])
            return
    print(L[0],R[-1])
    return
