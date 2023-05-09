def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] == i + 1:
            ans += 1
    if ans == N:
        print(0)
    elif ans == N - 1:
        print(1)
    else:
        print(N - ans)
main()
