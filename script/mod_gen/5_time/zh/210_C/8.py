def main():
    n, k = map(int, input().split())
    candies = list(map(int, input().split()))
    #print(n, k, candies)
    candy_set = set()
    for i in range(n-k+1):
        candy_set.add(len(set(candies[i:i+k])))
    print(max(candy_set))

if __name__ == '__main__':
    main()