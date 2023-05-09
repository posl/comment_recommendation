def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'R':
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
    max_count = max(count, max_count)
    print(max_count)

if __name__ == '__main__':
    main()