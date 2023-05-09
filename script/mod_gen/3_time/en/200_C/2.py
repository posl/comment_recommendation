def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    cnt = [0] * 200
    for a in A:
        cnt[a] += 1
    ans = 0
    for c in cnt:
        ans += c * (c - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()