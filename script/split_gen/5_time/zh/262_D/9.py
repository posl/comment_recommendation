def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    ans += 1
                else:
                    break
    print(ans)
