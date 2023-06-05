def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    for i in range(n):
        if a[i] != i+1:
            print('No')
            break
    else:
        print('Yes')

if __name__ == '__main__':
    main()