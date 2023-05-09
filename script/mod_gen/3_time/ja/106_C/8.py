def main():
    s = input()
    k = int(input())
    print(s[(k-1)//len(s)])

if __name__ == '__main__':
    main()