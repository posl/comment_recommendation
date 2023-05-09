def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i] == B[C[j]-1]:
                ans += 1
    print(ans)
