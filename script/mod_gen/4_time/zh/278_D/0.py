def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            for j in range(n):
                a[j] = int(query[1])
        elif query[0] == '2':
            a[int(query[1]) - 1] += int(query[2])
        else:
            print(a[int(query[1]) - 1])

if __name__ == '__main__':
    main()