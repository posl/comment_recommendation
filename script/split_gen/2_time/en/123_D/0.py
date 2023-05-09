def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ABC = []
    for a in A:
        for b in B:
            ABC.append(a+b)
    ABC.sort(reverse=True)
    ABC = ABC[:K]
    ABC2 = []
    for abc in ABC:
        for c in C:
            ABC2.append(abc+c)
    ABC2.sort(reverse=True)
    ABC2 = ABC2[:K]
    for abc2 in ABC2:
        print(abc2)
main()
