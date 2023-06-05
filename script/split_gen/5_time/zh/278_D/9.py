def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            for i in range(len(A)):
                A[i] = x
        elif query[0] == '2':
            i = int(query[1])
            x = int(query[2])
            A[i-1] += x
        else:
            i = int(query[1])
            print(A[i-1])
