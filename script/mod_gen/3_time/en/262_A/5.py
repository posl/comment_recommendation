def main():
    y = int(input())
    y += 4 - y % 4
    print(y)

if __name__ == '__main__':
    main()