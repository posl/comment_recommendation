def main():
    #read input
    n, m, q = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(m)]
    queries = [list(map(int, input().split())) for _ in range(q)]
    #process
    #sum[i][j] = number of trains that runs strictly within the section from City i to City j
    sum = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for train in trains:
        sum[train[0]][train[1]] += 1
    #cumulative sum
    for i in range(1, n+1):
        for j in range(1, n+1):
            sum[i][j] += sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]
    #output
    for query in queries:
        print(sum[query[1]][query[1]] - sum[query[0]-1][query[1]] - sum[query[1]][query[0]-1] + sum[query[0]-1][query[0]-1])
main()
