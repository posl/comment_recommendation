def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    min = a[0]
    for i in range(1,n):
        if a[i] < min:
            ans += 1
            min = a[i]
    print(ans)
