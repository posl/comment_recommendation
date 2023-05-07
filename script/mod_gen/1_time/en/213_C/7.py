def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    for i in range(n):
        print(a.index(a[i]) + 1, b.index(b[i]) + 1)

if __name__ == '__main__':
    main()