def main():
    k = int(input())
    print(''.join([chr(65 + i) for i in range(k)]))

if __name__ == '__main__':
    main()