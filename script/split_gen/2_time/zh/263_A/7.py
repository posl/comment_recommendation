def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if sum(a[i:j+1]) % (j - i + 1) == 0:
                ans += 1
    print(ans)
