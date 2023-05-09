def main():
    s = input()
    result = 0
    count = 0
    for i in s:
        if i in "ACGT":
            count += 1
        else:
            count = 0
        result = max(result, count)
    print(result)

if __name__ == '__main__':
    main()