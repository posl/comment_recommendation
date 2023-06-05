def main():
    a, N = map(int, input().split())
    ans = 0
    while N > 1:
        if N % a == 0:
            N //= a
        elif (N - 1) % a == 0:
            N = (N - 1) // a
        else:
            ans = -1
            break
        ans += 1
    print(ans)
