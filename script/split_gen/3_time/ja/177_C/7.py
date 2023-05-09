def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    ans = 0
    for i in range(N-1):
        ans += (A[i] * A[i+1]) * (N-1-i)
    print(ans % 1000000007)
