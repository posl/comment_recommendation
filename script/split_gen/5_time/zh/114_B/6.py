def main():
    S = input()
    S = [int(i) for i in S]
    min_diff = 753 - int(''.join([str(i) for i in S[:3]]))
    for i in range(1, len(S) - 2):
        diff = 753 - int(''.join([str(i) for i in S[i:i+3]]))
        if abs(diff) < abs(min_diff):
            min_diff = diff
    print(abs(min_diff))
