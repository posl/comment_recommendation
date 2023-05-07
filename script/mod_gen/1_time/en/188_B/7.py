def inner_product():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = 0
    for i in range(n):
        result += a[i] * b[i]
    if result == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    inner_product()