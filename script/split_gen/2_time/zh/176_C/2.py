def main():
    n = int(input())
    a = list(map(int,input().split()))
    max_a = 0
    ans = 0
    for i in range(n):
        if a[i] > max_a:
            max_a = a[i]
        else:
            ans += max_a - a[i]
    print(ans)
