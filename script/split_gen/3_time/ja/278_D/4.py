def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(Q):
        if query[i][0] == 1:
            sum += (query[i][1] - A[query[i][1]-1])
            A[query[i][1]-1] = query[i][1]
        elif query[i][0] == 2:
            sum += query[i][2]
            A[query[i][1]-1] += query[i][2]
        else:
            print(sum)
