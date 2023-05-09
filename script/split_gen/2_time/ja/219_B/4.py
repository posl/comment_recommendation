def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    S = [S1, S2, S3]
    for i in T:
        print(S[int(i)-1], end="")
