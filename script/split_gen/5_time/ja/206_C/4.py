def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    A.sort()
    #print(A)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] != A[j]:
                ans += 1
    print(ans)
