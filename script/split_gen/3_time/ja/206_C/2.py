def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i] != a[j]:
                ans += 1
    print(ans)
