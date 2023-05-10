def main():
    N, X = map(int, input().split())
    bags = []
    for i in range(N):
        bag = list(map(int, input().split()))
        bags.append(bag)
    ans = 0
    for i in range(1, 2**N):
        total = 1
        for j in range(N):
            if (i >> j) & 1:
                total *= bags[j][0]
        if total == X:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()