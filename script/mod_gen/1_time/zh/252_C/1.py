def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    # print(s)
    ans = 0
    for i in range(10):
        for j in range(n):
            if s[j][i] == str(i):
                break
            if j == n - 1:
                ans = ans + 1
    print(ans)

if __name__ == '__main__':
    main()