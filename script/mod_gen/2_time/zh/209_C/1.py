def main():
    N = 2
    C = [1, 3]
    ans = 1
    C.sort()
    for i in range(N):
        ans *= (C[i] - i)
        ans %= (10**9 + 7)
    print(ans)

if __name__ == '__main__':
    main()