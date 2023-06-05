def main():
    n, c = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i, c_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    print(n, c)
    print(a)
    print(b)

if __name__ == '__main__':
    main()