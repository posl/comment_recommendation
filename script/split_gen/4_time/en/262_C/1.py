def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if a[i-1] == i:
            ans += 1
    print(ans)
