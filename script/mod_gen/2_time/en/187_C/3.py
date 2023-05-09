def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S1 = set()
    S2 = set()
    for s in S:
        if s[0] == "!":
            S1.add(s[1:])
        else:
            S2.add(s)
    S3 = S1 & S2
    if len(S3) == 0:
        print("satisfiable")
    else:
        print(S3.pop())

if __name__ == '__main__':
    main()