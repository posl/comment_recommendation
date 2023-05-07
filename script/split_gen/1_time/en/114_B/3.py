def main():
    S = input()
    min_diff = 753
    for i in range(len(S)-2):
        min_diff = min(min_diff, abs(753 - int(S[i:i+3])))
    print(min_diff)
