def main():
    S = input()
    count = 0
    for i in range(0, int(len(S)/2)):
        if S[i] != S[-i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()