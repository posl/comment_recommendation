def main():
    S = [input() for i in range(10)]
    A = B = C = D = -1
    for i in range(10):
        if S[i].find('#') != -1:
            if A == -1:
                A = i + 1
            B = i + 1
            if C == -1:
                C = S[i].find('#') + 1
            D = max(D, S[i].rfind('#') + 1)
    print(A, B)
    print(C, D)
