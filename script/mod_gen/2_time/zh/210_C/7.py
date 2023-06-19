def main():
    n, k = map(int, input().split())
    candies = list(map(int, input().split()))
    max_kinds = 0
    for i in range(n-k+1):
        kinds = len(set(candies[i:i+k]))
        if kinds > max_kinds:
            max_kinds = kinds
    print(max_kinds)

if __name__ == '__main__':
    main()