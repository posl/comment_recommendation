def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    ans = 0
    for i in range(N):
        ans += A[i]/B[i]
    ans /= 2
    print(ans)
