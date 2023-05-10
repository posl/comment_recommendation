def main():
    n, l = map(int, input().split())
    taste = [l+i for i in range(n)]
    min_index = taste.index(min(taste, key=abs))
    print(sum(taste[:min_index]+taste[min_index+1:]))

if __name__ == '__main__':
    main()