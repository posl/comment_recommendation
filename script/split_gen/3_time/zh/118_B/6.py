def main():
    N,M = map(int,input().split())
    A = [[0 for i in range(0,M)] for j in range(0,N)]
    for i in range(0,N):
        A[i] = list(map(int,input().split()))
    #print(A)
    food = [0 for i in range(0,M)]
    for i in range(0,N):
        for j in range(1,A[i][0]+1):
            food[A[i][j]-1] += 1
    #print(food)
    count = 0
    for i in range(0,M):
        if food[i] == N:
            count += 1
    print(count)
