def main():
    s = input()
    acgt = "ACGT"
    count = 0
    max_count = 0
    for i in s:
        if i in acgt:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

if __name__ == '__main__':
    main()