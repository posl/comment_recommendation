def main():
    n = int(input())
    s = input()
    q = int(input())
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            a -= 1
            b -= 1
            s = s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]
        else:
            s = s[n:] + s[:n]
    print(s)

if __name__ == '__main__':
    main()