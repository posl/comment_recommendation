def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    c = 0
    for i in range(n):
        c += a[i] * b[i]
    if c == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()