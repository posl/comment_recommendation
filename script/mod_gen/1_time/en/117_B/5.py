def main():
    N = int(input())
    L = [int(x) for x in input().split()]
    L.sort(reverse=True)
    print('Yes' if L[0] < sum(L[1:]) else 'No')

if __name__ == '__main__':
    main()