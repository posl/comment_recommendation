def main():
    S = input()
    S = S.replace("?", "0")
    S = S.replace("A", "1")
    S = S.replace("B", "2")
    S = S.replace("C", "3")
    Q = S.count("0")
    S = int(S)
    mod = 10**9 + 7
    ans = 3**Q
    for i in range(Q):
        ans = (ans * 3) % mod
    print(ans)

if __name__ == '__main__':
    main()