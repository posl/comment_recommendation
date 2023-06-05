def main():
    n = int(input())
    s = input()
    ret = ""
    for c in s:
        x = ord(c) + n
        if x > ord('Z'):
            x = x - ord('Z') + ord('A') - 1
        ret += chr(x)
    print(ret)

if __name__ == '__main__':
    main()