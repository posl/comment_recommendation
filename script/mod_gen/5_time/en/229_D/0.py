def main():
    S = input()
    K = int(input())
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'X':
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(min(max_count+K, len(S)))

if __name__ == '__main__':
    main()