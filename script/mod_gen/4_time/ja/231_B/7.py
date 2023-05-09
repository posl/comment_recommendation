def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    #print(S)
    max = 0
    count = 0
    for i in range(N):
        if i == 0:
            count = 1
        else:
            if S[i] == S[i-1]:
                count += 1
            else:
                count = 1
        if max < count:
            max = count
            max_name = S[i]
    print(max_name)

if __name__ == '__main__':
    main()