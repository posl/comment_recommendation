def main():
    n = int(input())
    s = input()
    str = ''
    for i in s:
        if ord(i)+n > ord('Z'):
            str = str + chr(ord(i)+n-ord('Z')+ord('A')-1)
        else:
            str = str + chr(ord(i)+n)
    print(str)

if __name__ == '__main__':
    main()