def main():
    n = int(input())
    h = list(map(int, input().split()))
    i = 1
    max_h = h[0]
    while i < n:
        if h[i] >= h[i-1]:
            max_h = h[i]
        i += 1
    print(max_h)

if __name__ == '__main__':
    main()