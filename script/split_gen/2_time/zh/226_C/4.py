def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()))[1:])
    a.sort()
    ans = 0
    for i in range(n):
        if i == 0 or a[i] != a[i - 1]:
            ans += 1
    print(ans)
