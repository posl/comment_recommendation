def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i == 0 or a[i] != a[i-1]:
            for j in range(i+1, n):
                if a[j] % a[i] == 0:
                    break
            else:
                ans += 1
    print(ans)
