def main():
    S = input()
    K = int(input())
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'X':
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0
    if len(S) == max_count:
        print(max_count)
    elif max_count + K >= len(S):
        print(len(S))
    else:
        print(max_count + 2 * K + 1)

if __name__ == '__main__':
    main()