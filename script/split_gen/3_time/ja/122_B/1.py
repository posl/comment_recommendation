def main():
    S = input()
    max = 0
    count = 0
    for i in range(len(S)):
        if S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T':
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    if count > max:
        max = count
    print(max)
