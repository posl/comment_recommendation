def main():
    S = input()
    S = list(S)
    max_length = 0
    length = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            length += 1
        else:
            max_length = max(max_length, length)
            length = 0
    max_length = max(max_length, length)
    print(max_length)
