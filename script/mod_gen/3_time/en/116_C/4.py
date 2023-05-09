def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    count = 0
    while (sum(h) != 0):
        for i in range(n):
            if h[i] != 0:
                count += 1
                while (i < n and h[i] != 0):
                    h[i] -= 1
                    i += 1
    print(count)

if __name__ == '__main__':
    main()