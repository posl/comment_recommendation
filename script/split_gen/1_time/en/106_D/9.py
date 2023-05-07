def main():
    # read input
    n, m, q = map(int, input().split())
    train = [list(map(int, input().split())) for _ in range(m)]
    query = [list(map(int, input().split())) for _ in range(q)]
    # create array of 0s
    # array[i][j] = 0 if train j is not running between city i and i+1
    # array[i][j] = 1 if train j is running between city i and i+1
    array = [[0 for _ in range(m)] for _ in range(n)]
    # populate array
    for i in range(m):
        for j in range(train[i][0], train[i][1]):
            array[j-1][i] = 1
    # sum array for each query
    for i in range(q):
        print(sum(array[query[i][0]-1][query[i][1]-1]))
main()
