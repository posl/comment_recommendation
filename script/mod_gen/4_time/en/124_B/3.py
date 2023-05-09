def main():
    n = int(input())
    h = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if h[i] >= max(h[:i+1]):
            c += 1
    print(c)

if __name__ == '__main__':
    main()