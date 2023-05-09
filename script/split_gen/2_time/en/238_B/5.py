def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A = A[::-1]
    ans = 360
    for i in range(N):
        ans = min(ans, 360 - (ans - A[i]) % 360)
    print(ans)
