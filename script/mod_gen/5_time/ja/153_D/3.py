def main():
    h = int(input())
    cnt = 0
    while h > 0:
        cnt += 1
        h //= 2
    print(2 ** cnt - 1)

if __name__ == '__main__':
    main()