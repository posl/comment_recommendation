def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i]
        if ans <= 0:
            print(0)
            return
    print(ans)
