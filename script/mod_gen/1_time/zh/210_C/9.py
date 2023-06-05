def main():
    n, k = map(int, input().split())
    candy = list(map(int, input().split()))
    candy_set = set(candy[:k])
    max_candy = len(candy_set)
    for i in range(n - k):
        candy_set.add(candy[i + k])
        if len(candy_set) > max_candy:
            max_candy = len(candy_set)
        candy_set.remove(candy[i])
    print(max_candy)

if __name__ == '__main__':
    main()