def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = k // n
    B = sorted(A)
    for i in range(k % n):
        ans[B[i] - 1] += 1
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()