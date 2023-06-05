def main():
    N,K = map(int,input().split())
    S = input()
    L = []
    for i in range(N):
        if S[i] == "L":
            L.append(i)
    R = []
    for i in range(N):
        if S[i] == "R":
            R.append(i)
    A = []
    for i in range(len(L)-1):
        A.append(L[i+1]-L[i])
    B = []
    for i in range(len(R)-1):
        B.append(R[i+1]-R[i])
    if len(A) == 0 and len(B) == 0:
        print(N)
        return
    if len(A) == 0:
        A.append(100000)
    if len(B) == 0:
        B.append(100000)
    A.sort()
    B.sort()
    if len(A) == 1:
        print(min(N,A[0]+2*K))
        return
    if len(B) == 1:
        print(min(N,B[0]+2*K))
        return
    ans = 0
    for i in range(len(A)):
        if i == 0:
            ans = max(ans,A[i]+K)
        else:
            ans = max(ans,A[i]//2)
    for i in range(len(B)):
        if i == 0:
            ans = max(ans,B[i]+K)
        else:
            ans = max(ans,B[i]//2)
    print(min(N,ans+K))

if __name__ == '__main__':
    main()