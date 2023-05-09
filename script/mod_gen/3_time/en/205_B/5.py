def check_permutation():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n+1):
        if i != a[i-1]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    check_permutation()