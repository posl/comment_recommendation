def main():
    s = input()
    t = input()
    if s in t[:-1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()