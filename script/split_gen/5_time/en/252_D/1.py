def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] != A[j] and A[i] != A[k] and A[j] != A[k]:
                    if A[i] + A[j] > A[k]:
                        ans += 1
    print(ans)
