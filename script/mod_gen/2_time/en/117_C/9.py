def  main():
     # Input 
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
     # Sort 
    X.sort()
     # Calculate the distance between all adjacent coordinates 
    D = []
    for i in range(M - 1):
        D.append(X[i + 1] - X[i])
     # If the number of pieces is greater than or equal to the number of coordinates, 
     # the minimum number of moves is 0. 
    if N >= M:
        print(0)
        return
     # Sort in ascending order 
    D.sort()
     # The sum of the distances between the coordinates of the pieces 
    ans = sum(D[0:M - N])
    print(ans)
