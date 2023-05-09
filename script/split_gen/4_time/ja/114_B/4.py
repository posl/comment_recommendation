def main():
    # input
    S = input()
    # compute
    X = []
    for i in range(len(S)-2):
        X.append(abs(753-int(S[i:i+3])))
    # output
    print(min(X))
