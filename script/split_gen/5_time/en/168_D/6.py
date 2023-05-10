def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ans = [0] * n
    for a, b in ab:
        ans[a-1] += 1
        ans[b-1] += 1
    for v in ans:
        if v % 2:
            print('No')
            return
    print('Yes')
    for v in ans:
        print(1)
main()
