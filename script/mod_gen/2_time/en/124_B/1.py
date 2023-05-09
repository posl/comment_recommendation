def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 1
    for i in range(n-1):
        if h[i] <= h[i+1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()