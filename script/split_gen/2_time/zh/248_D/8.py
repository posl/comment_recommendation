def countx(lst, x):
    count = 0
    for ele in lst:
        if ele == x:
            count = count + 1
    return count
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
Query = []
for i in range(Q):
    Query.append(list(map(int, input().split())))
for i in range(Q):
    print(countx(A[Query[i][0]-1:Query[i][1]], Query[i][2]))
