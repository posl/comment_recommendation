def main():
    k = int(input())
    print(''.join([chr(i+65) for i in range(k)]))

if __name__ == '__main__':
    main()