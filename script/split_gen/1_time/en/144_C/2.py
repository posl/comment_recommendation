def main():
    N = int(input())
    ans = N-1
    for i in range(1, N):
        if N % i == 0:
            ans = min(ans, i+N//i-2)
    print(ans)
