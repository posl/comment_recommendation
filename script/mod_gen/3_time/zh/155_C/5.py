def main():
    n = int(input())
    S = []
    for i in range(n):
        S.append(input())
    S.sort()
    max_count = 0
    max_str = ""
    count = 0
    for i in range(n):
        if i == 0:
            count = 1
            max_count = 1
            max_str = S[i]
        else:
            if S[i] == S[i - 1]:
                count += 1
            else:
                count = 1
            if count > max_count:
                max_count = count
                max_str = S[i]
    print(max_str)

if __name__ == '__main__':
    main()