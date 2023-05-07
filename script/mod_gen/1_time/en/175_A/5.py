def main():
    S = input()
    max_count = 0
    count = 0
    for i in range(0, 3):
        if S[i] == 'R':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

if __name__ == '__main__':
    main()