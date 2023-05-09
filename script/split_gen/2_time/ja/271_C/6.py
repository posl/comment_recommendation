def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] >= ans + 1:
            ans += 1
    print(ans)
