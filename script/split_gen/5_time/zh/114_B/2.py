def main():
    S = input()
    num = len(S)
    min_diff = 753
    for i in range(num-2):
        x = int(S[i:i+3])
        diff = abs(x-753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
