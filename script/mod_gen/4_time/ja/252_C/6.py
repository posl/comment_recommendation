def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(s)
    ans = 0
    for i in range(n):
        ans += 1
        for j in range(10):
            if s[i][j] == str(i+1):
                break
    print(ans)

if __name__ == '__main__':
    main()