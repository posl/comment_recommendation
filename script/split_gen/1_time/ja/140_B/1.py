def main():
    n = int(input())
    a = [int(i) - 1 for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        ans += b[a[i]]
        if i != 0 and a[i] == a[i - 1] + 1:
            ans += c[a[i - 1]]
    print(ans)
