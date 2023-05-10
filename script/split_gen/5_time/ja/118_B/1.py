def main():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()))[1:])
    ans = 0
    for i in range(1, m+1):
        for j in range(n):
            if i not in a[j]:
                break
        else:
            ans += 1
    print(ans)
