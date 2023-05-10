def main():
    n, k, q = map(int, input().split())
    ans = [0] * n
    for _ in range(q):
        a = int(input())
        ans[a-1] += 1
    for i in range(n):
        if k - q + ans[i] > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()