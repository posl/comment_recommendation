def main():
    S = input()
    N = len(S)
    count = 0
    for i in range(N):
        if i == 0:
            if S[i] == S[i+1]:
                count += 1
        elif i == N-1:
            if S[i] == S[i-1]:
                count += 1
        else:
            if S[i] == S[i-1] or S[i] == S[i+1]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()