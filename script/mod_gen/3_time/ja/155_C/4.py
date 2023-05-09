def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    max = 0
    count = 0
    for i in range(N):
        if S[i] == S[i-1]:
            count += 1
        else:
            if count > max:
                max = count
            count = 1
    if count > max:
        max = count
    count = 0
    for i in range(N):
        if S[i] == S[i-1]:
            count += 1
        else:
            if count == max:
                print(S[i-1])
            count = 1
    if count == max:
        print(S[N-1])

if __name__ == '__main__':
    main()