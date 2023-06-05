def main():
    n, k = map(int, input().split())
    candies = list(map(int, input().split()))
    candy_set = set()
    max_candy = 0
    for i in range(n-k+1):
        for j in range(k):
            candy_set.add(candies[i+j])
        if len(candy_set) > max_candy:
            max_candy = len(candy_set)
        candy_set.clear()
    print(max_candy)

if __name__ == '__main__':
    main()