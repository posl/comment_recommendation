def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i % 2 == 0 and a[i] == a[i+1]:
            ans += 1
    print(ans)
