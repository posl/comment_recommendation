def main():
    n, q = map(int, input().split())
    s = list(input())
    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s.insert(0, s.pop(x - 1))
        else:
            print(s[x - 1])

if __name__ == '__main__':
    main()