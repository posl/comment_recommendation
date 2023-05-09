def main():
    S = input()
    count = 0
    maxCount = 0
    for i in range(len(S)):
        if S[i] == 'R':
            count += 1
        else:
            count = 0
        if count > maxCount:
            maxCount = count
    print(maxCount)

if __name__ == '__main__':
    main()