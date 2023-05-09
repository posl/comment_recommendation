def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_height = 0
    for i in range(n-1):
        if h[i+1] > h[i]:
            max_height = h[i+1]
    print(max_height)

if __name__ == '__main__':
    main()