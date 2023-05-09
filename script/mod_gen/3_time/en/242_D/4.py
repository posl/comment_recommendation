def main():
    S = input()
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    abc = [0, 0, 0]
    for s in S:
        abc[ord(s) - ord("A")] += 1
    for t, k in queries:
        t %= 3
        if t == 0:
            print("ABC"[abc.index(k)])
        elif t == 1:
            print("ABC"[abc.index(k + abc[0])])
        else:
            print("ABC"[abc.index(k + abc[0] + abc[1])])

if __name__ == '__main__':
    main()