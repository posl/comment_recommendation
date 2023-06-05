def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    print(a)
    print(b)
    print(m)

if __name__ == '__main__':
    main()