def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if N % i == 0:
            ans += N // i
    print(ans)
