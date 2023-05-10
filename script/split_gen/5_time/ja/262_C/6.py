def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] < i+1:
            continue
        for j in range(i+1, a[i]+1):
            if j <= a[j-1]:
                ans += 1
    print(ans)
