def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    ans = [k - q] * n
    for i in a:
        ans[i-1] += 1
    for i in ans:
        if i > 0:
            print('Yes')
        else:
            print('No')
main()
