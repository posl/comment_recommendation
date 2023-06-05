def main():
    n = int(input())
    d = {}
    for _ in range(n):
        l = list(map(int, input().split()))
        if len(l) > 1:
            l.pop(0)
        s = ''.join(map(str, l))
        d[s] = 1
    print(len(d))

if __name__ == '__main__':
    main()