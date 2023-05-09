def main():
    k = int(input())
    print(''.join([chr(x) for x in range(65, 65 + k)]))

if __name__ == '__main__':
    main()