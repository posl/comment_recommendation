def main():
    k = int(input().strip())
    print(''.join([chr(ord('A') + i) for i in range(k)]))

if __name__ == '__main__':
    main()