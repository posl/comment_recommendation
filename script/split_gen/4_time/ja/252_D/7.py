def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * (2*10**5+1)
    for i in range(N):
        B[A[i]] += 1
    ans = 0
    for i in range(2*10**5+1):
        if B[i] >= 3:
            ans += B[i]*(B[i]-1)*(B[i]-2)//6
        if B[i] >= 2:
            for j in range(i+1, 2*10**5+1):
                if B[j] >= 2:
                    ans += B[i]*B[j]*(B[j]-1)//2
        if B[i] >= 1:
            for j in range(i+1, 2*10**5+1):
                if B[j] >= 1:
                    ans += B[i]*B[j]*B[j]
    print(ans)
