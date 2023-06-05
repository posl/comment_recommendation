def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    q = int(input())
    for i in range(q):
        query = [int(i) for i in input().split()]
        if query[0] == 1:
            a[query[1]-1] = query[2]
        elif query[0] == 2:
            print(a[query[1]-1])

if __name__ == '__main__':
    main()