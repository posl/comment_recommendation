def main():
    # input
    n = int(input())
    l = list(map(int, input().split()))
    # output
    if max(l) < sum(l) - max(l):
        print('是')
    else:
        print('否')

if __name__ == '__main__':
    main()