def main():
    N,X = map(int,input().split())
    print(chr(X%N+64))

if __name__ == '__main__':
    main()