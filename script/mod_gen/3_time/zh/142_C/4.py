def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i+1
    print(' '.join(str(i) for i in b))

if __name__ == '__main__':
    main()