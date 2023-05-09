def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if i == 0:
            count += 1
        elif i > 0:
            if h[i] >= max(h[:i]):
                count += 1
    print(count)

if __name__ == '__main__':
    main()