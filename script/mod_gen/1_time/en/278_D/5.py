def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    cnt = 0
    for i in range(Q):
        if query[i][0] == 1:
            cnt += query[i][1]
        elif query[i][0] == 2:
            A[query[i][1]-1] += query[i][2]
        else:
            ans.append(A[query[i][1]-1] + cnt)
    for i in ans:
        print(i)
main()
