def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a + [0]
    ans = 0
    for i in range(1, n+2):
        if a[i-1] == a[i+1]:
            ans += 1
            a[i] = a[i-1]
    print(ans)
