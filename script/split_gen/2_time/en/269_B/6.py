def main():
    S = [input() for _ in range(10)]
    A = [i for i in range(10) if S[0][i] == '#']
    B = [i for i in range(10) if S[9][i] == '#']
    C = [i for i in range(10) if S[i][0] == '#']
    D = [i for i in range(10) if S[i][9] == '#']
    print(min(A)+1, max(A)+1, min(C)+1, max(C)+1, sep=' ')
    print(min(B)+1, max(B)+1, min(D)+1, max(D)+1, sep=' ')
