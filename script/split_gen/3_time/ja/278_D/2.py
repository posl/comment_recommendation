def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = []
    for _ in range(q):
        query.append(list(map(int, input().split())))
    ans = []
    for i in range(q):
        if query[i][0] == 1:
            for j in range(n):
                a[j] = query[i][1]
        elif query[i][0] == 2:
            a[query[i][1]-1] += query[i][2]
        else:
            ans.append(a[query[i][1]-1])
    for i in range(len(ans)):
        print(ans[i])
