def main():
    N = int(input())
    H = list(map(int,input().split()))
    count = 0
    maxcount = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            count = 0
        if count > maxcount:
            maxcount = count
    print(maxcount)

if __name__ == '__main__':
    main()