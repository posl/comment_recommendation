def main():
    S = input()
    N = len(S)
    min_753 = 753
    for i in range(N-2):
        X = int(S[i:i+3])
        if abs(X-753) < min_753:
            min_753 = abs(X-753)
    print(min_753)
