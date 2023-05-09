def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    for i in range(n-1):
        if s[i][0] == s[i+1][0]:
            print("satisfiable")
            exit()
    print("".join(s))

if __name__ == '__main__':
    main()