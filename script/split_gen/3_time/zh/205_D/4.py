def solve(n, q, a, k):
    # write your code here
    c = 0
    b = []
    for i in range(1, 10**18):
        if i not in a:
            c += 1
            b.append(i)
        if c == max(k):
            break
    return b[k-1]
    pass
n, q = map(int, input().split())
a = list(map(int, input().split()))
k = []
for i in range(q):
    k.append(int(input()))
print(solve(n, q, a, k))
