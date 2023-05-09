def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * (n + 1)
    for i in a:
        b[i] += 1
    ans = [0] * n
    for i in range(1, n+1):
        ans[i-1] = sum([b[j] for j in range(1, n+1) if j != i]) - b[i] + b[i] * (b[i] - 1) // 2
    print('
'.join(map(str, ans)))

if __name__ == '__main__':
    main()