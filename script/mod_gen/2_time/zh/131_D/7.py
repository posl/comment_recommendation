def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ab = zip(a, b)
    ab = sorted(ab, key=lambda x: x[1])
    a, b = zip(*ab)
    now = 0
    for i in range(n):
        now += a[i]
        if now > b[i]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()