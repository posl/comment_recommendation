def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = 0
    count = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            count += 1
        else:
            count = 0
        if count > max_h:
            max_h = count
    print(max_h)

if __name__ == '__main__':
    main()