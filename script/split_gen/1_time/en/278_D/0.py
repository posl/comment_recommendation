def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(str, input().split())))
    ans = []
    for i in range(Q):
        if query[i][0] == '1':
            A = [int(query[i][1])]*N
        elif query[i][0] == '2':
            A[int(query[i][1])-1] += int(query[i][2])
        else:
            ans.append(A[int(query[i][1])-1])
    for i in range(len(ans)):
        print(ans[i])
