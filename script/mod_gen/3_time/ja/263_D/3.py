def main():
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    A = sorted(A)
    #print(A)
    ans = 0
    for i in range(N):
        if A[i] < 0:
            ans += L
        else:
            ans += R
    print(ans)

if __name__ == '__main__':
    main()