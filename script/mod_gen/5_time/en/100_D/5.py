def main():
    n, m = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(2**3):
        xyz.sort(key=lambda x: sum([x[k] * (-1)**((i>>k)&1) for k in range(3)]), reverse=True)
        ans = max(ans, sum([sum([x[k] * (-1)**((i>>k)&1) for k in range(3)]) for x in xyz[:m]]))
    print(ans)

if __name__ == '__main__':
    main()