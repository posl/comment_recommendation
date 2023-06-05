def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    for i in range(n):
        b[a[i]] = i+1
    ans = 0
    for i in range(1, n+1):
        if b[i] == i:
            ans += 1
        else:
            if b[i] > b[i+1]:
                ans += 1
    print(ans)
