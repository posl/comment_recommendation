def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    # 1 x
    # 2 i x
    # 3 i
    add = 0
    ans = []
    for q in query:
        if q[0] == 1:
            add = q[1]
        elif q[0] == 2:
            A[q[1] - 1] += q[2]
        else:
            ans.append(A[q[1] - 1] + add)
    print(*ans, sep='
')
    return

if __name__ == '__main__':
    main()