def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    #print(A)
    table = [[0 for _ in range(2*N)] for _ in range(M+1)]
    for i in range(2*N):
        table[0][i] = i+1
    #print(table)
    for i in range(1, M+1):
        for j in range(N):
            #print(table[i-1][2*j-1], table[i-1][2*j])
            if A[table[i-1][2*j]-1][i-1] == A[table[i-1][2*j+1]-1][i-1]:
                table[i][2*j] = table[i-1][2*j]
                table[i][2*j+1] = table[i-1][2*j+1]
            elif A[table[i-1][2*j]-1][i-1] == "G" and A[table[i-1][2*j+1]-1][i-1] == "C":
                table[i][2*j] = table[i-1][2*j]
                table[i][2*j+1] = table[i-1][2*j+1]
            elif A[table[i-1][2*j]-1][i-1] == "C" and A[table[i-1][2*j+1]-1][i-1] == "P":
                table[i][2*j] = table[i-1][2*j]
                table[i][2*j+1] = table[i-1][2*j+1]
            elif A[table[i-1][2*j]-1][i-1] == "P" and A[table[i-1][2*j+1]-1][i-1] == "G":
                table[i][2*j] = table[i-1][2*j]
                table[i][2*j+1] = table[i-1][2*j+1]
            else:
                table[i][2*j] = table[i-1][2*j+1]
                table[i][2*j+1] = table[i-1][2*j]
    #print(table)
    for i in range(2*N):
        print(table[M][i])
