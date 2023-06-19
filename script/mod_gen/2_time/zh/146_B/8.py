def main():
    n = int(input())
    s = input()
    s = [chr(ord(i)+n) for i in s]
    s = [i if ord(i) <= ord('Z') else chr(ord(i)-26) for i in s]
    print(''.join(s))

if __name__ == '__main__':
    main()