def main():
    a, N = map(int, input().split())
    if N % a != 0:
        print(-1)
        return
    N //= a
    ans = 0
    while N > 0:
        if N % 10 == 1:
            N //= 10
        elif N % 2 == 0:
            N //= 2
        else:
            print(-1)
            return
        ans += 1
    print(ans)
