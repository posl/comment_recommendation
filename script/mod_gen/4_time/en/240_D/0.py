def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2 * 10 ** 5 + 1)
    for a in A:
        B[a] += 1
    ans = 0
    for i in range(1, 2 * 10 ** 5 + 1):
        ans = max(ans, B[i - 1] + B[i] + B[i + 1])
    print(ans)

if __name__ == '__main__':
    main()