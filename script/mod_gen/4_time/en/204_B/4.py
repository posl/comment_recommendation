def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    # compute
    nuts = 0
    for a in A:
        if a > 10:
            nuts += a - 10
    # output
    print(nuts)

if __name__ == '__main__':
    main()