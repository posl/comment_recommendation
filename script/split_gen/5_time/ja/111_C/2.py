def main():
    N = int(input())
    V = list(map(int, input().split()))
    A = V[0::2]
    B = V[1::2]
    import collections
    c1 = collections.Counter(A)
    c2 = collections.Counter(B)
    if c1.most_common()[0][0] == c2.most_common()[0][0]:
        if len(c1) == 1 and len(c2) == 1:
            print(N//2)
        else:
            print(N//2 - max(c1.most_common()[0][1], c2.most_common()[0][1]))
    else:
        print(N - c1.most_common()[0][1] - c2.most_common()[0][1])
main()
