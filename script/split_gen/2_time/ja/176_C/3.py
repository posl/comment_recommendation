def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    h = 0
    for i in range(1, n):
        if a[i] > a[i-1]:
            h += 1
        else:
            ans += h*(h+1)//2
            h = 0
    ans += h*(h+1)//2
    print(ans+n)
