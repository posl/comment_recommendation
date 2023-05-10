def main():
    n = int(input())
    l = []
    r = []
    for i in range(n):
        a, b = map(int, input().split())
        l.append(a)
        r.append(b)
    l.sort()
    r.sort()
    print(l[-1], r[0])

if __name__ == '__main__':
    main()