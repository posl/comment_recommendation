def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    max_h = 0
    for i in range(n):
        if h[i] >= max_h:
            max_h = h[i]
    print(max_h)

if __name__ == '__main__':
    main()