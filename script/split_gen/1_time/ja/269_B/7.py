def main():
    S = [input() for _ in range(10)]
    A, B, C, D = 1, 10, 1, 10
    for i in range(10):
        if S[i].count(".") == 10:
            A = i + 1
        if S[i].count("#") == 10:
            B = i
    for i in range(10):
        if S[0][i] == ".":
            C = i + 1
        if S[0][i] == "#":
            D = i
    print(A, B)
    print(C, D)
