def main():
    N = int(input())
    ans = 0
    for i in range(1, 16):
        if N >= 10 ** (3 * i):
            ans += 3 * 10 ** (3 * (i - 1))
        else:
            ans += (N - 10 ** (3 * (i - 1)) + 1) * i
            break
    print(ans)
main()
