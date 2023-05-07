def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = sorted(S)
    count = 1
    max_count = 0
    max_strings = []
    for i in range(N-1):
        if T[i] == T[i+1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_strings = [T[i]]
            elif count == max_count:
                max_strings.append(T[i])
            count = 1
    if count > max_count:
        max_count = count
        max_strings = [T[N-1]]
    elif count == max_count:
        max_strings.append(T[N-1])
    for s in max_strings:
        print(s)

if __name__ == '__main__':
    main()