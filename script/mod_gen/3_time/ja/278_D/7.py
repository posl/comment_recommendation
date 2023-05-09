def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    query3s = [q for q in queries if q[0] == 3]
    query3s.sort(key=lambda x: x[1])
    query3s = [q[1] for q in query3s]
    query3s = list(set(query3s))
    query3s.sort()
    query3s = [q-1 for q in query3s]
    #print(query3s)
    query3s.reverse()
    query3s = set(query3s)
    #print(query3s)
    A = [0] + A
    #print(A)
    for q in queries:
        if q[0] == 1:
            A = [q[1]] * (N+1)
        elif q[0] == 2:
            A[q[1]] += q[2]
        elif q[0] == 3:
            if q[1] in query3s:
                print(A[q[1]])
                query3s.remove(q[1])
    return

if __name__ == '__main__':
    main()