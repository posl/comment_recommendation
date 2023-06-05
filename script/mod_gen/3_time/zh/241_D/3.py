def main():
    q = int(input())
    a = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            a.append(x)
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            b = [i for i in a if i <= x]
            if len(b) < k:
                print(-1)
            else:
                b.sort(reverse=True)
                print(b[k-1])
        else:
            x = int(query[1])
            k = int(query[2])
            b = [i for i in a if i >= x]
            if len(b) < k:
                print(-1)
            else:
                b.sort()
                print(b[k-1])

if __name__ == '__main__':
    main()