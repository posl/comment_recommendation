def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i][0] == "!":
            s[i] = s[i][1:]
    s.sort()
    for i in range(n-1):
        if s[i] == s[i+1]:
            print(s[i])
            exit()
    print("satisfiable")

if __name__ == '__main__':
    main()