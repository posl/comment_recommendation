def main():
    L, Q = map(int, input().split())
    cuts = []
    for i in range(Q):
        cuts.append(list(map(int, input().split())))
    cuts.sort(key=lambda x: x[0])
    cuts.sort(key=lambda x: x[1])
    print(cuts)
    for i in range(Q):
        if cuts[i][0] == 1:
            cuts[i][0] = 0
        else:
            cuts[i][0] = 1
    print(cuts)
    cuts = [x for x in cuts if x[0] == 0]
    print(cuts)
    cuts.sort(key=lambda x: x[1])
    print(cuts)
    cuts.insert(0, [0, 0])
    cuts.append([0, L])
    print(cuts)
    for i in range(1, len(cuts)):
        cuts[i][1] -= cuts[i - 1][1]
    print(cuts)
    for i in range(1, len(cuts)):
        cuts[i][1] += cuts[i - 1][1]
    print(cuts)
    for i in range(1, len(cuts)):
        cuts[i][1] -= cuts[i - 1][1]
    print(cuts)
    cuts = [x[1] for x in cuts]
    print(cuts)
    cuts.sort()
    for i in range(len(cuts)):
        if cuts[i] == 0:
            cuts[i] = cuts[i + 1]
    print(cuts)
    for i in range(len(cuts)):
        if cuts[i] == 0:
            cuts[i] = cuts[i - 1]
    print(cuts)
    cuts = [x for x in cuts if x != 0]
    print(cuts)
    for i in range(len(cuts)):
        print(cuts[i])

if __name__ == '__main__':
    main()