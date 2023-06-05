def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = h[0]
    for i in range(1, n):
        if h[i] > max_h:
            max_h = h[i]
    print(max_h)

if __name__ == '__main__':
    main()