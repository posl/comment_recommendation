def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(k):
        if a[0] == a[b[i] - 1]:
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()