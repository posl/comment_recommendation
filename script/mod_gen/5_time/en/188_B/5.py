def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        a[i] *= b[i]
    if sum(a) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()