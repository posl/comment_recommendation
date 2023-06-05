def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    count = {}
    for i in range(n):
        x = a[i]
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
        if count[x] == x:
            ans[i] = 1
        else:
            ans[i] = 0
    for i in range(n):
        print(ans[i])
