def main():
    # input
    S = input()
    # solve
    min_diff = 1000
    for i in range(len(S)-2):
        X = int(S[i:i+3])
        diff = abs(X-753)
        if diff < min_diff:
            min_diff = diff
    # output
    print(min_diff)
    return
