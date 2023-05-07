def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    ans = []
    for i in range(q):
        if query[i][0] == 1:
            a = [query[i][1]] * n
        elif query[i][0] == 2:
            a[query[i][1] - 1] += query[i][2]
        else:
            ans.append(a[query[i][1] - 1])
    print(*ans, sep='
')
