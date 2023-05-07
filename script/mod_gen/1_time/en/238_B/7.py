def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 答えを求める
    ans = 360
    for i in range(N):
        ans = min(ans, abs(360 - 2 * sum(A[:i+1])))
    print(ans)

if __name__ == '__main__':
    main()