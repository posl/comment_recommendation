def main():
    n = int(input())
    a = list(map(int, input().split()))
    # b = 0 の時の悲しさ
    b = 0
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (b + i + 1))
    # b = 1 の時の悲しさ
    b = 1
    tmp = 0
    for i in range(n):
        tmp += abs(a[i] - (b + i + 1))
    # b = 1 の時の悲しさが最小の場合
    if tmp < ans:
        ans = tmp
    # b = -1 の時の悲しさ
    b = -1
    tmp = 0
    for i in range(n):
        tmp += abs(a[i] - (b + i + 1))
    # b = -1 の時の悲しさが最小の場合
    if tmp < ans:
        ans = tmp
    print(ans)

if __name__ == '__main__':
    main()