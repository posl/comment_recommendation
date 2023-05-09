def main():
    N, X = map(int, input().split())
    print(chr(64+X//N))

if __name__ == '__main__':
    main()