def main():
    S = input()
    b = 0
    w = 0
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == '0':
                b += 1
            else:
                w += 1
        else:
            if S[i] == '0':
                w += 1
            else:
                b += 1
    print(min(b, w))

if __name__ == '__main__':
    main()