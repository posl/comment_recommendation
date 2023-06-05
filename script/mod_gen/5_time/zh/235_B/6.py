def main():
    n = int(input())
    h = list(map(int, input().split()))
    max = 0
    for i in range(n):
        if h[i] >= max:
            max = h[i]
    print(max)

if __name__ == '__main__':
    main()