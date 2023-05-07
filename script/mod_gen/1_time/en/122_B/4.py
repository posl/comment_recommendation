def main():
    s = input()
    count = 0
    max_count = 0
    for i in s:
        if i in 'ACGT':
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    max_count = max(max_count, count)
    print(max_count)

if __name__ == '__main__':
    main()