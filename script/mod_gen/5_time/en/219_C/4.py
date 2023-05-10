def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    x = sorted(x)
    for i in range(n):
        s[i] = sorted(s[i], key=x.index)
    s = sorted(s)
    for i in range(n):
        print(''.join(s[i]))

if __name__ == '__main__':
    main()