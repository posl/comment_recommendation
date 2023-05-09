def main():
    N = int(input())
    ans = 0
    z = 2
    while z*z <= N:
        while N % z == 0:
            N //= z
            ans += 1
        z += 1
    if N > 1:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()