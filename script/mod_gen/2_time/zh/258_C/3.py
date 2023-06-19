def main():
    n, q = map(int, input().split())
    s = input()
    for i in range(q):
        t, x = map(int, input().split())
        if t == 2:
            print(s[x-1])
        else:
            s = s[n-x:] + s[:n-x]

if __name__ == '__main__':
    main()