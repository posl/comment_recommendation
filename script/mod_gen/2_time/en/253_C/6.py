def main():
    Q = int(input())
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            print(x)
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            print(x, c)
        elif query[0] == '3':
            print('3')

if __name__ == '__main__':
    main()