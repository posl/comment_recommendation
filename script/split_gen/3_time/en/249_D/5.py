def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(N):
                if A[i] * A[j] == A[k]:
                    ans += 1
    print(ans)
