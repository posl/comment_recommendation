def main():
    s = input()
    for i in range(len(s)+1):
        if s == s[::-1]:
            print('Yes')
            break
        else:
            s = 'a'+s
    else:
        print('No')

if __name__ == '__main__':
    main()