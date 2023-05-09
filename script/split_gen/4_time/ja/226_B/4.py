def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    a.sort()
    a.append([0, 0])
    ans = 1
    for i in range(n):
        if a[i] != a[i + 1]:
            ans += 1
    print(ans)
