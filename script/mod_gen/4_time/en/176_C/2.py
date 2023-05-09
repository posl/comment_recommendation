def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_height = 0
    stools = 0
    for i in range(n):
        if a[i] >= max_height:
            stools += a[i] - max_height
            max_height = a[i]
        else:
            max_height = a[i]
    print(stools)

if __name__ == '__main__':
    main()