def main():
    N = int(input())
    votes = [input() for _ in range(N)]
    count = {}
    for vote in votes:
        if vote in count:
            count[vote] += 1
        else:
            count[vote] = 1
    count_sorted = sorted(count.items(), key=lambda x: x[1], reverse=True)
    max_vote = count_sorted[0][1]
    for k, v in count_sorted:
        if v == max_vote:
            print(k)

if __name__ == '__main__':
    main()