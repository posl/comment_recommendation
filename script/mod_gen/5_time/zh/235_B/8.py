def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = 0
    for i in range(n-1):
        if h[i] < h[i+1]:
            max_h = h[i+1]
    print(max_h)

if __name__ == '__main__':
    main()