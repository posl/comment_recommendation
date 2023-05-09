def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    for q in query:
        if q[0] == 1:
            A = [q[1]]*N
        elif q[0] == 2:
            A[q[1]-1] += q[2]
        elif q[0] == 3:
            ans.append(A[q[1]-1])
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()