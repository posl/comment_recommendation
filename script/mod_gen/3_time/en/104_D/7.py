def main():
    S = input()
    mod = 10 ** 9 + 7
    Q = S.count('?')
    ans = 0
    for i in range(Q):
        ans = (ans * 3 + pow(3, Q - i - 1, mod)) % mod
    print(ans)

if __name__ == '__main__':
    main()