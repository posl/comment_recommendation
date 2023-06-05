def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum([x*y for x, y in zip(a, b)]) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()