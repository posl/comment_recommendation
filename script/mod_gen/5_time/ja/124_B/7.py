def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max = 0
    for i in range(n):
        if h[i] >= max:
            count += 1
            max = h[i]
    print(count)

if __name__ == '__main__':
    main()