def main():
    N = int(input())
    L = list(map(int, input().split()))
    maxL = max(L)
    sumL = sum(L)
    if maxL < sumL - maxL:
        print('是')
    else:
        print('否')

if __name__ == '__main__':
    main()