def main():
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            for j in range(n):
                A[j] = query[1]
        elif query[0] == 2:
            A[query[1]-1] += query[2]
        elif query[0] == 3:
            print(A[query[1]-1])
