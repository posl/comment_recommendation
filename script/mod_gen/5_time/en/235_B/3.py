def main():
    n = int(input())
    h = list(map(int, input().split()))
    i = 0
    while i < n - 1:
        if h[i] < h[i + 1]:
            h[i + 1] -= 1
            i = 0
        else:
            i += 1
    print(h[n - 1])

if __name__ == '__main__':
    main()