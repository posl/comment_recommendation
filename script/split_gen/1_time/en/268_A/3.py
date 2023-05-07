def main():
    # read input
    A, B, C, D, E = map(int, input().split())
    # make set
    s = set()
    s.add(A)
    s.add(B)
    s.add(C)
    s.add(D)
    s.add(E)
    # print result
    print(len(s))
