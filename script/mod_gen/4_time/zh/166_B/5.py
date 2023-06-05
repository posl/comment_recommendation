def main():
    n, k = map(int, input().split())
    # 零食的集合
    snacks = set()
    for i in range(k):
        d = int(input())
        a = list(map(int, input().split()))
        for j in range(d):
            snacks.add(a[j])
    # 没有零食的人
    no_snacks = n - len(snacks)
    print(no_snacks)

if __name__ == '__main__':
    main()