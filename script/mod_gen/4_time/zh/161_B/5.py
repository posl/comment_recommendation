def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    s = sum(A)
    for i in range(m):
        if A[i] < s / (4 * m):
            print('否')
            exit()
    print('是')

if __name__ == '__main__':
    main()