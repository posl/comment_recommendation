def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for q in range(Q):
        query.append(input().split())
    
    for q in query:
        if q[0] == '1':
            for i in range(N):
                A[i] = int(q[1])
        elif q[0] == '2':
            A[int(q[1]) - 1] += int(q[2])
        else:
            print(A[int(q[1]) - 1])
