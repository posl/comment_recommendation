def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [a[i]*b[i] for i in range(n)]
    if sum(c) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()