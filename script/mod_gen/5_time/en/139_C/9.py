def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    #print(N)
    #print(H)
    count = 0
    max_count = 0
    for i in range(1,N):
        if H[i-1] >= H[i]:
            count = count + 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    print(max_count)

if __name__ == '__main__':
    main()