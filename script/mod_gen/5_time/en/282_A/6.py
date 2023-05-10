def main():
    input = int(raw_input())
    print ''.join([chr(i) for i in range(65, 65+input)])

if __name__ == '__main__':
    main()