def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1001):
        if all(a[j] <= i <= b[j] for j in range(n)):
            ans += 1
    print(ans)
