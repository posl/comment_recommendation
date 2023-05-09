def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if a[i] == a[j]:
                continue
            for k in range(j+1, n):
                if a[j] == a[k]:
                    continue
                if a[i] == a[k]:
                    continue
                if a[i] + a[j] > a[k]:
                    ans += 1
                else:
                    break
    print(ans)
