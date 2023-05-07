def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    # 1
    for q in query:
        if q[0] == 1:
            x = q[1]
            for i in range(N):
                A[i] = x
        # 2
        elif q[0] == 2:
            A[q[1]-1] += q[2]
        # 3
        else:
            ans.append(A[q[1]-1])
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()