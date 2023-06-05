def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if (A[i]+A[j])%2==0 and (A[i]+A[j])//2 in A:
                ans += 1
    print(ans)
