def main():
    # input
    N = int(input())
    a = list(map(int, input().split()))
    # compute
    a_set = set(a)
    # output
    print(len(a_set))

if __name__ == '__main__':
    main()