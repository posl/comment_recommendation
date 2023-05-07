def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    #print(A)
    #print(N, M)
    #print(A[0][0])
    #print(A[1][0])
    #print(A[2][0])
    #print(A[3][0])
    #print("")
    # 2N players, with ID numbers 1 through 2N, will participate in a rock-scissors-paper contest.
    # The contest has M rounds. Each round has N one-on-one matches, where each player plays in one of them.
    # For each i=0, 1, ..., M, the players' ranks at the end of the i-th round are determined as follows.
    # A player with more wins in the first i rounds ranks higher.
    # Ties are broken by ID numbers: a player with a smaller ID number ranks higher.
    # Additionally, for each i=1, ..., M, the matches in the i-th round are arranged as follows.
    # For each k=1, 2, ..., N, a match is played between the players who rank (2k-1)-th and 2k-th at the end of the (i-1)-th round.
    # In each match, the two players play a hand just once, resulting in one player's win and the other's loss, or a draw.
    # Takahashi, who can foresee the future, knows that Player i will play A_{i, j} in their match in the j-th round, where A_{i,j} is G, C, or P.
    # Here, G stands for rock, C stands for scissors, and P stands for paper. (These derive from Japanese.)
    # Find the players' ranks at the end of the M-th round.
    # Rules of rock-scissors-paper
    # The result of a rock-scissors-paper match is determined as follows, based on the hands played by the two players.
    # If one player plays rock (G) and the other plays scissors (C), the player playing rock (G) wins.
    # If one player plays scissors (C) and the other plays paper (P), the player playing scissors (C) wins.
    # If one player plays paper (P) and the other plays rock (G),

if __name__ == '__main__':
    main()