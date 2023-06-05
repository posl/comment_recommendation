def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for i in range(q)]
    a.sort()
    s = sum(a)
    for i in range(q):
        s += x[i]
        print(s)
        if s < 0:
            s = sum(a)
        else:
            s += x[i] * n

if __name__ == '__main__':
    main()