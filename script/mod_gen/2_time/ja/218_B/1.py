def main():
    p = list(map(int, input().split()))
    alphabet = [chr(ord('a') + i - 1) for i in p]
    print(''.join(alphabet))

if __name__ == '__main__':
    main()