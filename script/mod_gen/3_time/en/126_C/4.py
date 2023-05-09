def main():
    n, k = map(int, input().split())
    p = 0
    for i in range(1, n+1):
        if i >= k:
            p += 1/n
        else:
            p += 1/n * (1/2)**(len(bin(k-i))-2)
    print(p)

if __name__ == '__main__':
    main()