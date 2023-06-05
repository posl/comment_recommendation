def main():
    N = int(input())
    ans = 0
    for i in range(2, N):
        if N % i == 0:
            ans += 1
            N = N // i
            if N == 1:
                break
    print(ans)
