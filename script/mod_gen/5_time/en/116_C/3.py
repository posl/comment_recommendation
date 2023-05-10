def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.append(0)
    count = 0
    for i in range(n):
        if h[i] < h[i+1]:
            count += h[i+1] - h[i]
    print(count)

if __name__ == '__main__':
    main()