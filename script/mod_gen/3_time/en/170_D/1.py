def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    ans = 0
    for i in range(1, 10**6):
        cnt = 0
        for j in range(i, 10**6+1, i):
            cnt += c[j]
        if cnt == 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()