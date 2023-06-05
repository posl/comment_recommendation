def main():
    n,l = map(int,input().split())
    min_sum = 1000000000
    for i in range(1,n+1):
        if min_sum > abs(l+i-1):
            min_sum = abs(l+i-1)
            min_index = i
    sum = 0
    for i in range(1,n+1):
        if i != min_index:
            sum += l+i-1
    print(sum)

if __name__ == '__main__':
    main()