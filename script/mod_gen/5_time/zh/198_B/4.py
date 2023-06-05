def main():
    num = input()
    num = num[::-1]
    print('Yes' if num == num[::-1] else 'No')

if __name__ == '__main__':
    main()