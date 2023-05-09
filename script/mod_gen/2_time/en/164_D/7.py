def main():
    S = input()
    S = S[::-1]
    count = 0
    for i in range(4):
        if S[i] == '1':
            count += 1
    for i in range(4, len(S)):
        if S[i] == '1':
            count += 1
        if S[i] == '2':
            count += 1
    print(count)

if __name__ == '__main__':
    main()