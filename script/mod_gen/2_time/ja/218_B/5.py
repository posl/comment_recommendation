def main():
    p = list(map(int, input().split()))
    p = [chr(ord('a') + i - 1) for i in p]
    print(''.join(p))

if __name__ == '__main__':
    main()