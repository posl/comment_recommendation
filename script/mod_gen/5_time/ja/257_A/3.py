def main():
    n,x = map(int,input().split())
    print(chr(ord('A') + (x-1) % 26) * n)

if __name__ == '__main__':
    main()