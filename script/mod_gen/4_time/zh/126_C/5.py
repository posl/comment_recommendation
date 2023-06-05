def main():
    n, k = map(int, input().split())
    p = 0
    for i in range(1, n+1):
        j = 0
        while i * (2 ** j) < k:
            j += 1
        p += (1/n) * (1/2) ** j
    print(p)

if __name__ == '__main__':
    main()