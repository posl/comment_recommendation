def main():
    n = int(input())
    h = list(map(int, input().split()))
    max = h[0]
    for i in range(1, n):
        if max < h[i]:
            max = h[i]
    print(h.index(max)+1)

if __name__ == '__main__':
    main()