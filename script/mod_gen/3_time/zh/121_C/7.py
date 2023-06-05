def main():
    N, M = map(int, input().split())
    l = []
    for i in range(N):
        a, b = map(int, input().split())
        l.append((a, b))
    l.sort()
    s = 0
    for a, b in l:
        if M <= b:
            s += a * M
            break
        s += a * b
        M -= b
    print(s)

if __name__ == '__main__':
    main()