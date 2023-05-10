def main():
    n, m = map(int, input().split())
    a = [input() for i in range(2*n)]
    b = [(i, 0) for i in range(2*n)]
    for i in range(m):
        c = []
        for j in range(n):
            a1, a2 = b[2*j]
            b1, b2 = b[2*j+1]
            if a[a1][i] == a[b1][i]:
                continue
            elif a[a1][i] == 'G':
                if a[b1][i] == 'C':
                    c.append((a1, 1))
                    c.append((b1, -1))
                elif a[b1][i] == 'P':
                    c.append((a1, -1))
                    c.append((b1, 1))
            elif a[a1][i] == 'C':
                if a[b1][i] == 'P':
                    c.append((a1, 1))
                    c.append((b1, -1))
                elif a[b1][i] == 'G':
                    c.append((a1, -1))
                    c.append((b1, 1))
            elif a[a1][i] == 'P':
                if a[b1][i] == 'G':
                    c.append((a1, 1))
                    c.append((b1, -1))
                elif a[b1][i] == 'C':
                    c.append((a1, -1))
                    c.append((b1, 1))
        c.sort(key=lambda x: x[0])
        c.sort(key=lambda x: x[1], reverse=True)
        b = c
    for i, j in b:
        print(i+1)

if __name__ == '__main__':
    main()