def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    if L[0] < sum(L[1:]):
        print('是')
    else:
        print('否')

if __name__ == '__main__':
    main()