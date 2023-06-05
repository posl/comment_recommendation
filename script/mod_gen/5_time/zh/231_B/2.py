def main():
    n = int(input())
    votes = []
    for i in range(n):
        votes.append(input())
    print(max(votes, key=votes.count))

if __name__ == '__main__':
    main()