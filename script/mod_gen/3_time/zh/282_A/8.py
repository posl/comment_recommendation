def main():
    k = int(input())
    s = ''
    for i in range(k):
        s += chr(i + ord('A'))
    print(s)

if __name__ == '__main__':
    main()