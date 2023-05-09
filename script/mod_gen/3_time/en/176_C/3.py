def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] > i:
            ans += A[i] - i
    print(ans)

if __name__ == '__main__':
    main()