def main():
    N = int(input())
    ans = 0
    z = 2
    while z <= N:
        while N % z == 0:
            ans += 1
            N = N // z
        z += 1
    print(ans)

if __name__ == '__main__':
    main()