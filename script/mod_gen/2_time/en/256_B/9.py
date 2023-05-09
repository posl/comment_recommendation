def main():
    #read input
    n = int(input())
    a = [int(x) for x in input().split()]
    #initialize variables
    p = 0
    board = [0, 0, 0, 0]
    #perform operations
    for i in range(n):
        board[0] += 1
        for j in range(4):
            if board[j] > 0:
                if j + a[i] < 4:
                    board[j + a[i]] += board[j]
                else:
                    p += board[j]
                board[j] = 0
    #print output
    print(p)

if __name__ == '__main__':
    main()