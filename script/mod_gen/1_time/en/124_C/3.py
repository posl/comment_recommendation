def main():
    S = input()
    N = len(S)
    count = 0
    for i in range(N):
        if i % 2 == 0:
            if S[i] == '0':
                count += 1
        else:
            if S[i] == '1':
                count += 1
    print(count)

if __name__ == '__main__':
    main()