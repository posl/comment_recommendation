def main():
    s = input().split()
    t = input().split()
    for i in range(3):
        if s[i] != t[i]:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()