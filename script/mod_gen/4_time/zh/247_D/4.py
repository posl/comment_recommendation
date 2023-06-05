def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    left = 0
    right = 0
    sum = 0
    for i in range(Q):
        if query[i][0] == 1:
            right = right + query[i][2]
            sum = sum + query[i][1] * query[i][2]
        else:
            sum = sum - query[i][1] * query[i][2]
            left = left + query[i][2]
        print(sum)

if __name__ == '__main__':
    main()