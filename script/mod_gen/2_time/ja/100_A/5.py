def main():
    A, B = map(int, input().split())
    print('Yay!' if A + B <= 16 and A <= 8 and B <= 8 else ':(')

if __name__ == '__main__':
    main()