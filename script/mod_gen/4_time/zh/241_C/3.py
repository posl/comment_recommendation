def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    # print(s)
    for i in range(1, n-1):
        for j in range(1, n-1):
            if s[i][j] == '#':
                if s[i-1][j] == '#' and s[i+1][j] == '#' and s[i][j-1] == '#' and s[i][j+1] == '#':
                    print("Yes")
                    return
    print("No")
    return

if __name__ == '__main__':
    main()