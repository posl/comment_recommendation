def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    print("Yes" if sum(b) >= x - (n - 1) else "No")

if __name__ == '__main__':
    main()