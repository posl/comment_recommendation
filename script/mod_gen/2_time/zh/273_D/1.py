def main():
    h, w, r, c = map(int, input().split())
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    q = int(input())
    b = []
    for _ in range(q):
        b.append(list(input().split())))
    print(h, w, r, c)
    print(n)
    print(a)
    print(q)
    print(b)

if __name__ == '__main__':
    main()