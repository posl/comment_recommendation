def main():
    S = input()
    min_diff = 753
    for i in range(len(S) - 2):
        diff = abs(int(S[i:i + 3]) - 753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
