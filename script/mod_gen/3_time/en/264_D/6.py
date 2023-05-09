def main():
    s = list(input())
    atcoder = list("atcoder")
    ans = 0
    for i in range(7):
        for j in range(i, 8):
            if s[i] == atcoder[j]:
                ans += j - i
                s[i], s[j] = s[j], s[i]
                break
    print(ans)

if __name__ == '__main__':
    main()