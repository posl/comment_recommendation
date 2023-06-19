def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    c = sorted(zip(b, a))
    t = 0
    for i in c:
        t += i[1]
        if t > i[0]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()