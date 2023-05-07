def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    for i in range(Q):
        query = [int(x) for x in input().split()]
        if query[0] == 1:
            A[query[1]-1] = query[2]
        else:
            print(A[query[1]-1])
