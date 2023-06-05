def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1001):
        for j in range(n):
            if a[j] <= i and i <= b[j]:
                ans += 1
                break
    print(ans)
