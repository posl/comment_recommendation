def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    ans = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1] - 1] = query[2]
        elif query[0] == 2:
            ans.append(a[query[1] - 1])
    print(*ans, sep='
')
