def main():
    N = int(input())
    S = input()
    if S.count('1') % 2 == 1:
        print('高桥')
    else:
        print('青木')

if __name__ == '__main__':
    main()