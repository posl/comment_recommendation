def main():
    x = input()
    m = int(input())
    d = int(max(x))
    n = d+1
    while True:
        if int(x, n) > m:
            break
        n += 1
    print(n-d-1)

if __name__ == '__main__':
    main()