def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    query = [list(map(int,input().split())) for _ in range(Q)]
    #print(N,A,Q,query)
    
    add = 0
    for q in query:
        if q[0] == 1:
            add = q[1]
        elif q[0] == 2:
            A[q[1]-1] += q[2] - add
        else:
            print(A[q[1]-1] + add)

if __name__ == '__main__':
    main()