def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()][1:])
    a.sort()
    ans = 1
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            ans += 1
    print(ans)
main()
