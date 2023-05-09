def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        if sum(p[i]) + 300 * (3 - len(p[i])) >= sum(sorted([sum(p[j]) for j in range(n) if i != j])[-k:]):
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()