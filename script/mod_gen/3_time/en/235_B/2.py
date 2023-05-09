def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = 0
    count = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            count = 0
        if count > max_h:
            max_h = count
    print(max_h+1)

if __name__ == '__main__':
    main()