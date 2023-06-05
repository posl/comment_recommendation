def main():
    X = int(input())
    print(int(X/500)*1000 + int((X%500)/5)*5)

if __name__ == '__main__':
    main()