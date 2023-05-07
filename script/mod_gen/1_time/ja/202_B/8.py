def main():
    S = input()
    print(S[::-1].replace('6','a').replace('9','6').replace('a','9'))

if __name__ == '__main__':
    main()