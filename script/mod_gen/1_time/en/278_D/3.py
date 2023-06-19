def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    ans = []
    add = 0
    for q in query:
        if q[0] == '1':
            add = int(q[1])
        elif q[0] == '2':
            A[int(q[1])-1] += int(q[2]) - add
        else:
            ans.append(A[int(q[1])-1] + add)
    print(*ans, sep='
')
main()
