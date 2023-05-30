def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    ans = [0] * n
    for i in range(1, n + 1):
        ans[a[i] - 1] += 1
    for i in ans:
        print(i)
main()
