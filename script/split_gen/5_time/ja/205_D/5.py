def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    ans = []
    for i in range(q):
        ans.append(k[i] + i)
    count = 0
    for i in range(q):
        for j in range(n):
            if ans[i] <= a[j]:
                count += 1
                break
    for i in range(q):
        print(ans[i] + count)
