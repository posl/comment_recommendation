def main():
    n, m = map(int, input().split())
    ans = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        ans[a-1].append(b)
        ans[b-1].append(a)
    for a in ans:
        print(len(a), *sorted(a))

if __name__ == '__main__':
    main()