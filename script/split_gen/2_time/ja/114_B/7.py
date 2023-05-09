def main():
    S = input()
    N = len(S)
    min_diff = 999
    for i in range(N-2):
        X = int(S[i:i+3])
        diff = abs(753 - X)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
