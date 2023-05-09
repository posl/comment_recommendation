def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = A[0]
    for i in range(1, N):
        if A[i] >= ans:
            ans += 1
        else:
            ans = A[i]
    print(ans)
