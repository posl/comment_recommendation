def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [i % 200 for i in A]
    C = [B.count(i) for i in set(B)]
    ans = 0
    for i in C:
        ans += i * (i - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()