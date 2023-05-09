def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        ans += (N//i) * (i-1)
        ans += max(0, N%i - i//2)
    print(ans)
