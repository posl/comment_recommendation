def main():
    S = input()
    min_diff = 1000
    for i in range(0, len(S)-2):
        diff = abs(int(S[i:i+3])-753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
