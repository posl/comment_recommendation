def main():
    S = input()
    T = input()
    pairs = []
    for i in range(len(S)):
        pairs.append([S[i], T[i]])
    pairs.sort()
    for i in range(len(pairs)-1):
        if pairs[i][0] == pairs[i+1][0] and pairs[i][1] != pairs[i+1][1]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()