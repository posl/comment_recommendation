def main():
    N = int(input())
    p = [int(i) for i in input().split()]
    c = 0
    for i in range(N):
        if p[i] != i+1:
            c += 1
    if c <= 2:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()