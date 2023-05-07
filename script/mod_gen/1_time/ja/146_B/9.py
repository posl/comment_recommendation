def main():
    N = int(input())
    S = input()
    result = ""
    for s in S:
        ascii_num = ord(s)
        ascii_num += N
        if ascii_num > 90:
            ascii_num -= 26
        result += chr(ascii_num)
    print(result)

if __name__ == '__main__':
    main()