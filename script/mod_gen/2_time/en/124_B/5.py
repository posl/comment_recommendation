def main():
    n = int(input())
    h = list(map(int, input().split()))
    c = 0
    for i in range(1, n):
        if max(h[0:i]) <= h[i]:
            c += 1
    print(c+1)

if __name__ == '__main__':
    main()