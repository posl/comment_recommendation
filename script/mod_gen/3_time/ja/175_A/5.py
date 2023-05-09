def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(3):
        if S[i] == 'R':
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0
    if max_count < count:
        max_count = count
    print(max_count)

if __name__ == '__main__':
    main()