def main():
    N,D = map(int,input().split())
    L = [0]*N
    R = [0]*N
    for i in range(N):
        L[i],R[i] = map(int,input().split())
    #print(N,D)
    #print(L)
    #print(R)
    L.sort()
    R.sort()
    #print(L)
    #print(R)
    ans = 0
    for i in range(N):
        if L[i] + D - 1 < R[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()