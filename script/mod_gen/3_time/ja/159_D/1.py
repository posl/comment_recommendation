def main():
    N = int(input())
    A = list(map(int, input().split()))
    c = [0] * (N + 1)
    for a in A:
        c[a] += 1
    ans = 0
    for a in c:
        ans += a * (a - 1) // 2
    for a in A:
        print(ans - c[a] + 1)

if __name__ == '__main__':
    main()