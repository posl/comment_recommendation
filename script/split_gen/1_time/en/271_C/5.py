def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != 1:
        print(0)
    else:
        ans = 1
        for i in range(1, N):
            if A[i] == A[i-1] + 1:
                ans += 1
            elif A[i] != A[i-1]:
                break
        print(ans)
    return
