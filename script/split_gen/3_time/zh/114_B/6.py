def main():
    S = input()
    N = len(S)
    min_diff = 1e9
    for i in range(N-2):
        x = int(S[i:i+3])
        diff = abs(753 - x)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
