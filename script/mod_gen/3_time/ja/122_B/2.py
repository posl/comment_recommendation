def main():
    S = input()
    max = 0
    count = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            count += 1
            if max < count:
                max = count
        else:
            count = 0
    print(max)

if __name__ == '__main__':
    main()