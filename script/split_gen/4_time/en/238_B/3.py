def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A[::-1]
    ans = 360
    for i in range(N):
        ans = ans - A[i]
    print(ans)
