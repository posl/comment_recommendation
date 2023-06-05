def main():
    S = input()
    S = list(S)
    count = 0
    max_count = 0
    for i in range(3):
        if S[i] == 'R':
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0
    print(max_count)

if __name__ == '__main__':
    main()