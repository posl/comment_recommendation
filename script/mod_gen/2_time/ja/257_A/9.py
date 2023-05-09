def main():
    n,x = map(int,input().split())
    print(chr(64+n+(x-n)%26))

if __name__ == '__main__':
    main()