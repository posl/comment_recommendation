def main():
    N = int(input())
    votes = [input() for _ in range(N)]
    votes.sort()
    count = 1
    max_count = 0
    max_count_name = ""
    for i in range(1, N):
        if votes[i] == votes[i-1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_count_name = votes[i-1]
            count = 1
    if count > max_count:
        max_count = count
        max_count_name = votes[-1]
    print(max_count_name)

if __name__ == '__main__':
    main()