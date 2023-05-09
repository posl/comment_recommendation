def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = -1
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] == A[i+1]:
                ans = A[i]
    print(ans)
