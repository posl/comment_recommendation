def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += (a[i] - a[j]) ** 2
    print(ans)
