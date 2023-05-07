def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n//2):
        if a[i] == a[n-1-i]:
            continue
        elif a[i] == a[n-2-i] and a[i+1] == a[n-1-i]:
            ans += 1
        else:
            ans += 1
    print(ans)
