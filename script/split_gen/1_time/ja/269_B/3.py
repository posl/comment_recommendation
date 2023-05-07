def main():
    S = [input() for _ in range(10)]
    A = 1
    B = 10
    C = 1
    D = 10
    for i in range(10):
        if S[i][0] == "#":
            A = i+1
            break
    for i in range(10):
        if S[i][9] == "#":
            B = i+1
            break
    for j in range(10):
        if S[0][j] == "#":
            C = j+1
            break
    for j in range(10):
        if S[9][j] == "#":
            D = j+1
            break
    print(A,B)
    print(C,D)
