def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                continue
            for k in range(j+1, n):
                if a[i] == a[k] or a[j] == a[k]:
                    continue
                if a[i] + a[j] > a[k]:
                    ans += 1
    print(ans)
