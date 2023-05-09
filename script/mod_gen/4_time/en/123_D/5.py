def main():
    # input
    X, Y, Z, K = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    Cs = list(map(int, input().split()))
    # compute
    # output
    print('Yes' if As[0] < Bs[0] < Cs[0] else 'No')

if __name__ == '__main__':
    main()