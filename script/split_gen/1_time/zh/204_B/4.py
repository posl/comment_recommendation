def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    ans = 0
    for i in range(N):
        if A[i] > 10:
            ans += A[i] - 10
    print(ans)
