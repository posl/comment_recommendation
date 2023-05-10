def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input())))
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                continue
            ans = max(ans, a[i][j]*1000+a[i][j+1]*100+a[i][j-1]*10+a[i+1][j]+a[i-1][j])
    print(ans)
