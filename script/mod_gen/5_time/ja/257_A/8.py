def main():
    n,x = map(int,input().split())
    print(chr(64+x//n))

if __name__ == '__main__':
    main()