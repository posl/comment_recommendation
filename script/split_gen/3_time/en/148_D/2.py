def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    if A[0] != 0:
        print(-1)
        return
    ans = 0
    for i in range(N):
        if A[i] > A[i + 1]:
            print(-1)
            return
        elif A[i] < A[i + 1]:
            ans += 1
        else:
            ans += 1
    print(ans)
