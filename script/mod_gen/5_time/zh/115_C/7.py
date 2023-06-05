def main():
    n,k = map(int, input().split())
    h = []
    for i in range(n):
        h.append(int(input()))
    h.sort()
    # print(h)
    min = h[k-1] - h[0]
    for i in range(n-k+1):
        if h[i+k-1] - h[i] < min:
            min = h[i+k-1] - h[i]
    print(min)

if __name__ == '__main__':
    main()