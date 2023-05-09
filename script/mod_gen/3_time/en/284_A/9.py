def main():
    n = int(input())
    print('
'.join([input() for i in range(n)][::-1]))

if __name__ == '__main__':
    main()