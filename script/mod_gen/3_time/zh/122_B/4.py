def main():
    S = input()
    max_length = 0
    for i in range(len(S)):
        length = 0
        for j in range(i, len(S)):
            if S[j] in 'ACGT':
                length += 1
            else:
                break
        if max_length < length:
            max_length = length
    print(max_length)

if __name__ == '__main__':
    main()