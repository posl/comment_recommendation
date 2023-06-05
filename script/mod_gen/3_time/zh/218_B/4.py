def main():
    p = list(map(int, input().split()))
    print(''.join(chr(ord('a') + x - 1) for x in p))

if __name__ == '__main__':
    main()