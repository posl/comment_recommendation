def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for _ in range(Q):
        query.append(list(map(int, input().split())))
    
    ans = sum(A)
    for q in query:
        if q[0] == 1:
            ans += (N * q[1])
        elif q[0] == 2:
            ans += q[1] * A[q[1] - 1]
            A[q[1] - 1] += q[2]
        else:
            print(A[q[1] - 1])
