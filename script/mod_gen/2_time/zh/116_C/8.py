def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    while True:
        if max(h) == 0:
            break
        else:
            for i in range(n):
                if h[i] > 0:
                    count += 1
                    h[i] -= 1
    print(count)

if __name__ == '__main__':
    main()