def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    ans = [0] * n
    for i in range(q):
        ans[a[i] - 1] += 1
    for i in range(n):
        if k - q + ans[i] > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()