def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if min(a[i-1], a[j-1]) == i and max(a[i-1], a[j-1]) == j:
                ans += 1
    print(ans)
