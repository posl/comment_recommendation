def main():
    # Read the data
    N, M = map(int, input().split())
    k = [0] * M
    x = [[0] * N for i in range(M)]
    for i in range(M):
        k[i], *x[i] = map(int, input().split())
    #print(N, M, k, x)
    # Solve the problem
    # Initialize the array
    attended = [[0] * N for i in range(N)]
    #print(attended)
    # Fill the array
    for i in range(M):
        for j in range(k[i]):
            for l in range(k[i]):
                attended[x[i][j] - 1][x[i][l] - 1] = 1
    #print(attended)
    # Check if the array is filled
    for i in range(N):
        for j in range(N):
            if attended[i][j] == 0:
                print("No")
                return
    # Print the answer
    print("Yes")
