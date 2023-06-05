def main():
    s = input()
    n, q = map(int, input().split())
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s = s[n-x:] + s[:n-x]
        else:
            print(s[x-1])

if __name__ == '__main__':
    main()