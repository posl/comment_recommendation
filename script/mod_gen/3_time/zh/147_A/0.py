def main():
    a = sum(map(int, input().split()))
    print('bust' if a >= 22 else 'win')

if __name__ == '__main__':
    main()