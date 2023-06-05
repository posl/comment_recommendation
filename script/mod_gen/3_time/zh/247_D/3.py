def main():
    # Q = int(input())
    # for i in range(Q):
    #     query = input().split()
    #     if query[0] == '1':
    #         x = int(query[1])
    #         c = int(query[2])
    #     else:
    #         c = int(query[1])
    #     print(c)
    #     print(x)
    #     print(query)
    Q = int(input())
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            c = int(query[2])
        else:
            c = int(query[1])
        print(c)
        print(x)
        print(query)

if __name__ == '__main__':
    main()