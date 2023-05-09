def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    ans = [0] * N
    cnt = 0
    for q in queries:
        if q[0] == 1:
            cnt = q[1]
        elif q[0] == 2:
            ans[q[1]-1] += q[2]
        else:
            print(A[q[1]-1] + cnt + ans[q[1]-1])

if __name__ == '__main__':
    main()