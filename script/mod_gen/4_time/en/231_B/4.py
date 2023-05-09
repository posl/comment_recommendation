def main():
    n = int(input())
    votes = [input() for i in range(n)]
    print(max(set(votes), key=votes.count))

if __name__ == '__main__':
    main()