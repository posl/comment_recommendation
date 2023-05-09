def main():
    N = int(input())
    ans = 0
    for i in range(1,16):
        if N >= 10**i:
            ans += (N - 10**(i-1) + 1) - 10**(i-1)
        else:
            ans += max(0, N - 10**(i-1) + 1)
        if i % 3 == 0:
            ans += 10**(i-1)
    print(ans)
