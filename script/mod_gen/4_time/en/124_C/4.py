def main():
    S = input()
    c = 0
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == '0':
                c += 1
        else:
            if S[i] == '1':
                c += 1
    print(min(c, len(S) - c))

if __name__ == '__main__':
    main()