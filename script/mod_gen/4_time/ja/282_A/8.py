def main():
    k = int(input())
    print("".join(list(map(chr, range(65, 65+k)))))

if __name__ == '__main__':
    main()