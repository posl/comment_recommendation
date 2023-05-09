def main():
    #input
    N = int(input())
    S = [input() for _ in range(N)]
    #count votes
    candidates = {}
    for s in S:
        if s not in candidates:
            candidates[s] = 0
        candidates[s] += 1
    #find winner
    winner = max(candidates, key=candidates.get)
    #output
    print(winner)
main()

if __name__ == '__main__':
    main()