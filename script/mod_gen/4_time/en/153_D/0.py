def main():
    h = int(input())
    count = 0
    while h > 0:
        count += 2 ** (h.bit_length() - 1)
        h -= 2 ** (h.bit_length() - 1)
    print(count)

if __name__ == '__main__':
    main()