def main():
    S = input()
    abs_min = 753
    for i in range(len(S)-2):
        abs_min = min(abs_min, abs(int(S[i:i+3])-753))
    print(abs_min)
