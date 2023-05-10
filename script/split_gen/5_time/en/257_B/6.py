def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = []
    for i in range(q):
        l.append(int(input()))
    # print(n, k, q)
    # print(a)
    # print(l)
    ans = [0] * n
    for i in range(q):
        ans[l[i] - 1] += 1
    # print(ans)
    for i in range(n):
        if k - (q - ans[i]) > 0:
            print("Yes")
        else:
            print("No")
