def main():
    print(input().translate(str.maketrans('01689', '61980'))[::-1])

if __name__ == '__main__':
    main()