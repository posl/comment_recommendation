def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A.append(N+1)
    #print(A)
    if M == 0:
        print(1)
        return
    if N == M:
        print(0)
        return
    if N == M+1:
        print(1)
        return
    ans = 0
    lis = []
    for i in range(1,M+1):
        if A[i] - A[i-1] - 1 > 0:
            lis.append(A[i] - A[i-1] - 1)
    lis.sort()
    #print(lis)
    ans = lis[0]
    for i in range(1,len(lis)):
        ans += lis[i] - 1
    print(ans)
    return
