def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for x in range(1, 1001):
        for i in range(n):
            if not (a[i] <= x <= b[i]):
                break
        else:
            ans += 1
    print(ans)
