def main():
    n, m = map(int, input().split())
    a = [[0] for i in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    #print(a)
    ans = 0
    for i in range(1, m + 1):
        for j in range(n):
            if i in a[j][1:]:
                if j == n - 1:
                    ans += 1
            else:
                break
    print(ans)
