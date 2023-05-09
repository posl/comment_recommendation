def main():
    # Read input
    N = int(input())
    S = [input() for i in range(N)]
    
    # Find the candidate with most votes
    most_votes = 0
    winner = ""
    for i in range(N):
        count = 0
        for j in range(N):
            if S[i] == S[j]:
                count += 1
        if count > most_votes:
            most_votes = count
            winner = S[i]
    
    # Print the winner
    print(winner)

if __name__ == '__main__':
    main()