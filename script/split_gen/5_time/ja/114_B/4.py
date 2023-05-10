def main():
    S = input()
    S_len = len(S)
    min_diff = 1000
    for i in range(S_len-2):
        diff = abs(753 - int(S[i:i+3]))
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
