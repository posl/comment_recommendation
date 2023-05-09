def main():
    # input
    N = int(input())
    ds = [*map(int, input().split())]
    # compute
    ds.sort()
    K = ds[N//2]
    # output
    print(K-ds[N//2-1])

if __name__ == '__main__':
    main()