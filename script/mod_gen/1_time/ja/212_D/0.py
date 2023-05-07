def main():
    Q = int(input())
    min_num = 0
    add_num = 0
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            min_num = min(min_num, query[1] - add_num)
        elif query[0] == 2:
            add_num += query[1]
        else:
            print(min_num + add_num)

if __name__ == '__main__':
    main()