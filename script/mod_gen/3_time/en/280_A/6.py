def main():
    # input
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # compute
    # output
    print(sum([s.count("#") for s in S]))

if __name__ == '__main__':
    main()