def main():
    n, q = map(int, input().split())
    x = [int(input()) for _ in range(q)]
    ans = list(range(1, n+1))
    for i in range(q-1, -1, -1):
        tmp = ans[x[i]-1]
        ans[x[i]-1] = ans[x[i]]
        ans[x[i]] = tmp
    print(*ans)
