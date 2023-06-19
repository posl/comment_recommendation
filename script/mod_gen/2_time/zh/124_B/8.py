def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(0, n):
        if i == 0 or max(h[0:i]) <= h[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()