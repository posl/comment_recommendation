def main():
    n = int(input())
    i = 1
    j = 1
    while i * j < n:
        if i > j:
            j += 1
        else:
            i += 1
    print(i + j - 2)

if __name__ == '__main__':
    main()