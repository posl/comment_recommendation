def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            a = [x for i in range(n)]
        elif query[0] == 2:
            i = query[1]
            x = query[2]
            a[i-1] += x
        else:
            i = query[1]
            print(a[i-1])

if __name__ == '__main__':
    main()