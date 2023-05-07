def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = a.copy()
    for i in range(1, n):
        c = []
        for j in range(0, 2**(n - i)):
            c.append(max(b[2*j], b[2*j+1]))
        b = c.copy()
    print(a.index(min(b[0], b[1])) + 1)

if __name__ == '__main__':
    main()