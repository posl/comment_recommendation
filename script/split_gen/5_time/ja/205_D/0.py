def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    ans = []
    for i in range(q):
        ans.append(k[i] + i)
    count = 0
    for i in range(n):
        if count < q and a[i] == ans[count]:
            count += 1
    for i in range(q):
        ans[i] += count
    for i in range(q):
        print(ans[i])
