def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    s = sum(a)
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s += query[1]*n
        elif query[0] == 2:
            s += query[1]
        else:
            print(s + a[query[1]-1])

if __name__ == '__main__':
    main()