def main():
    S = input()
    ans = 0
    idx = 0
    for c in "atcoder":
        idx = S.find(c, idx)
        if idx == -1:
            print(-1)
            exit()
        ans += idx
        idx += 1
    print(ans)

if __name__ == '__main__':
    main()