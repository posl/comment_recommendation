def main():
    N,K = map(int,input().split())
    ans = 0
    if K % 2 == 0:
        A = N // K
        ans += A ** 3
        if N >= K//2:
            B = (N - K//2) // K + 1
            ans += B ** 3
    else:
        A = N // K
        ans += A ** 3
    print(ans)
