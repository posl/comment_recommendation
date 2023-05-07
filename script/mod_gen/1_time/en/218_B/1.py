def main():
    P = list(map(int, input().split()))
    print(''.join([chr(ord('a') + p - 1) for p in P]))

if __name__ == '__main__':
    main()