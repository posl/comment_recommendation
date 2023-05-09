def main():
    n, k, a = map(int, input().split())
    if k >= n:
        k = k % n
    if k < n:
        if a + k > n:
            print(a + k - n)
        else:
            print(a + k)

if __name__ == '__main__':
    main()