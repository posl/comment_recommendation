def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 1
    max_h = h[0]
    for i in range(1, n):
        if h[i] >= max_h:
            cnt += 1
            max_h = h[i]
    print(cnt)

if __name__ == '__main__':
    main()