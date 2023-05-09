def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i != n-1 and a[i] == a[i+1]:
            continue
        ans += n-i-1
    print(ans)
