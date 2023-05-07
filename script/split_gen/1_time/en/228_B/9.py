def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    X -= 1
    
    count = 0
    visited = [False]*N
    i = X
    while not visited[i]:
        visited[i] = True
        i = A[i]-1
        count += 1
    print(count)
