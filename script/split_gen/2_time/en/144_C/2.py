def main():
    N = int(input())
    ans = N-1
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            ans = min(ans, N//i + i - 2)
    print(ans)
