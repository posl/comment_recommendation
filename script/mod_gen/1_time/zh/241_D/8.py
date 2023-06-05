def main():
    n = int(input())
    a = []
    for _ in range(n):
        query = input().split()
        if query[0] == '1':
            a.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            b = sorted(a)
            if x > b[-1]:
                print(-1)
            else:
                c = b.index(x) + k - 1
                if c >= len(b):
                    print(-1)
                else:
                    print(b[c])
        elif query[0] == '3':
            x = int(query[1])
            k = int(query[2])
            b = sorted(a)
            if x < b[0]:
                print(-1)
            else:
                c = b.index(x) - k + 1
                if c < 0:
                    print(-1)
                else:
                    print(b[c])

if __name__ == '__main__':
    main()