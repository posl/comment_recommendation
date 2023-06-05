def main():
    S = input()
    max_length = 0
    length = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            length += 1
        else:
            length = 0
        if length > max_length:
            max_length = length
    print(max_length)

if __name__ == '__main__':
    main()