def main():
    k = int(input())
    s = ''
    for i in range(k):
        s += chr(65+i)
    print(s)

if __name__ == '__main__':
    main()