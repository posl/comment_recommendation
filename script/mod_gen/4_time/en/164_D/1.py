def main():
    s = input()
    l = len(s)
    ans = 0
    for i in range(l):
        for j in range(i, l):
            if int(s[i:j+1]) % 2019 == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()