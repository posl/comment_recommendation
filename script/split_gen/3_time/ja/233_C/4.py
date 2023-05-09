def main():
    N,X = map(int,input().split())
    A = []
    for i in range(N):
        a = list(map(int,input().split()))
        A.append(a)
    #print(A)
    ans = 0
    for i in range(2**N):
        tmp = 1
        for j in range(N):
            if (i>>j) & 1:
                tmp *= A[j][1]
            else:
                tmp *= A[j][2]
        if tmp <= X:
            ans += 1
    print(ans)
