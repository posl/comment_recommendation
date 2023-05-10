def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(x)
    #print(n)
    #print(s)
    for i in range(n):
        s[i] = s[i].translate(str.maketrans(x, "abcdefghijklmnopqrstuvwxyz"))
    #print(s)
    s.sort()
    #print(s)
    for i in range(n):
        s[i] = s[i].translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", x))
    #print(s)
    for i in range(n):
        print(s[i])

if __name__ == '__main__':
    main()