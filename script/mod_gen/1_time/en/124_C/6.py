def main():
    S = input()
    count = 0
    if S == "0" or S == "1":
        print(count)
    else:
        for i in range(len(S)):
            if i == 0:
                if S[i] == "0":
                    count += 1
            else:
                if S[i] != S[i-1]:
                    count += 1
        print(count)

if __name__ == '__main__':
    main()