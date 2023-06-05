def main():
    n,k = input().split()
    n = int(n)
    k = int(k)
    a = input().split()
    b = input().split()
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    max_a = max(a)
    max_b = max(b)
    if max_a > max_b:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()