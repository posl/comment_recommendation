def main():
    n, m = [int(x) for x in input().split()]
    matrix = [[0 for x in range(n)] for y in range(n)]
    for i in range(m):
        a, b = [int(x) for x in input().split()]
        matrix[a-1][b-1] = 1
        matrix[b-1][a-1] = 1
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[k][i] == 1:
                    count += 1
    print(count)
