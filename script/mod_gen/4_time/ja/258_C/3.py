def main():
    n, q = map(int, input().split())
    s = input()
    s = list(s)
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s.insert(0, s.pop())
        else:
            print(s[x - 1])

if __name__ == '__main__':
    main()