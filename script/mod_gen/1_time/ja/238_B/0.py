def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 360
    for i in range(N):
        ans = min(ans, 360 - sum(A[:i+1]))
    print(ans)

if __name__ == '__main__':
    main()