def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N-M+1):
        B = A[i:i+M]
        tmp = 0
        for j in range(len(B)):
            tmp += (j+1)*B[j]
        if tmp > ans:
            ans = tmp
    print(ans)
