def main():
    S = [input() for i in range(10)]
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        if S[i][0] == '#':
            A = i+1
            break
    for i in range(10):
        if S[9-i][0] == '#':
            B = 10-i
            break
    for j in range(10):
        if S[0][j] == '#':
            C = j+1
            break
    for j in range(10):
        if S[0][9-j] == '#':
            D = 10-j
            break
    print(A,B)
    print(C,D)
