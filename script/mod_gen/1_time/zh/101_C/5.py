def main():
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    min_num = min(A)
    min_index = A.index(min_num)
    if min_index < k:
        if n % (k-1) == 0:
            print(n//(k-1))
        else:
            print(n//(k-1)+1)
    elif min_index >= k:
        if (n-min_index) % (k-1) == 0:
            print((n-min_index)//(k-1))
        else:
            print((n-min_index)//(k-1)+1)

if __name__ == '__main__':
    main()