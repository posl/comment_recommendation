def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    flag = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
            flag = 1
        else:
            count = 0
    print(count)

if __name__ == '__main__':
    main()