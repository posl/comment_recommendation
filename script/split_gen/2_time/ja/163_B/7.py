def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = N
    for i in range(M):
        ans -= A[i]
        if ans < 0:
            print("-1")
            return
    print(ans)
