def main():
    a = input()
    count = 0
    max_count = 0
    for i in range(3):
        if a[i] == "R":
            count += 1
        else:
            count = 0
        max_count = max(count, max_count)
    print(max_count)

if __name__ == '__main__':
    main()