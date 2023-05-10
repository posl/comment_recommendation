def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    friends = [0] * (n + 1)
    friends[x] = 1
    for i in range(1, n + 1):
        if friends[i] == 1:
            friends[a[i]] = 1
    print(sum(friends))

if __name__ == '__main__':
    main()