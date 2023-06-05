def main():
    n = int(input())
    s = input()
    if s.count('1') % 2 == 1:
        print('高桥')
    else:
        print('青木')

if __name__ == '__main__':
    main()