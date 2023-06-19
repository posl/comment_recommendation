def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = 0
    i = 0
    while i < n:
        if a[i] == a[i + 1]:
            ans += 1
            i += 2
        else:
            i += 1
    print(ans)
