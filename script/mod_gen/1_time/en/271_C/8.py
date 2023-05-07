def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for a in A:
        if a > ans + 1:
            break
        ans += a
    print(ans + 1)

if __name__ == '__main__':
    main()