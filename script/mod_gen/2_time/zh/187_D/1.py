def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a = sorted(a)
    b = sorted(b)
    max_a = a[-1]
    max_b = b[-1]
    if max_a >= max_b:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()