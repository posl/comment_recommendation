def main():
    import sys
    n = int(sys.stdin.readline().strip())
    k = 0
    while True:
        if 2 ** k > n:
            break
        k += 1
    print(k - 1)

if __name__ == '__main__':
    main()