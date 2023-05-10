def main():
    s = input()
    if s in 'o'*len(s)*2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()