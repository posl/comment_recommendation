def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(n):
            if a[i] % a[j] == 0:
                ans += 1
    print(ans)
