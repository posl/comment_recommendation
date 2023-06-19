def main():
    n = int(input())
    for i in range(0, n, 4):
        if (n - i) % 7 == 0:
            print('Yes')
            return
    print('No')
    return

if __name__ == '__main__':
    main()