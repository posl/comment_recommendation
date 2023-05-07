def main():
    s = input()
    print(ord(s[0])-ord('A')+1+26*(len(s)-1))

if __name__ == '__main__':
    main()