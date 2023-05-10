def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = sum(a)
    if a[0] < 0:
        ans -= 2*a[0]
    elif a[0] == 0:
        ans = 0
    else:
        ans -= 2*a[0]
        if a.count(0) % 2 == 1:
            ans = ans + 2*a[0]
    print(ans)
