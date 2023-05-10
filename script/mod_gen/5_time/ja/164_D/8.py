def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i+3,n):
            t = int(s[i:j+1])
            if t % 2019 == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()