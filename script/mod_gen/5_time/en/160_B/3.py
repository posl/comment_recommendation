def main():
    x = int(input())
    print(int(x/500)*1000 + int((x%500)/5)*5)

if __name__ == '__main__':
    main()