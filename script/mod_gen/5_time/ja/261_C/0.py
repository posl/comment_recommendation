def main():
    N = int(input())
    S = [input() for i in range(N)]
    S2 = []
    for i in range(N):
        if S[i] in S2:
            index = S2.count(S[i])
            S2.append(S[i]+"("+str(index)+")")
        else:
            S2.append(S[i])
    for i in range(N):
        print(S2[i])

if __name__ == '__main__':
    main()