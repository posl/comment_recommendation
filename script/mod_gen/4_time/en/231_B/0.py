def main():
    n = int(input())
    votes = {}
    
    for i in range(n):
        vote = input()
        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1
    
    print(max(votes, key=votes.get))

if __name__ == '__main__':
    main()