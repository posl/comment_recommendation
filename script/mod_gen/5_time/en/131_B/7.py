def main():
    N, L = map(int, input().split())
    apples = [L+i for i in range(N)]
    if L >= 0:
        print(sum(apples) - apples[0])
    elif L < 0 and L+N-1 >= 0:
        print(sum(apples))
    else:
        print(sum(apples) - apples[-1])

if __name__ == '__main__':
    main()