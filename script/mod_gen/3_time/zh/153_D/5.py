def main():
    h = int(input())
    count = 1
    while h > 1:
        count = count * 2
        h = h // 2
    print(count)

if __name__ == '__main__':
    main()