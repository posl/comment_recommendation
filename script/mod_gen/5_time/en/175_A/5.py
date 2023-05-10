def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(0, 3):
        if S[i] == 'R':
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)

if __name__ == '__main__':
    main()