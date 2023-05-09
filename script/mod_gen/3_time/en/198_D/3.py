def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = S1 + S2 + S3
    S = list(set(S))
    if len(S) > 10:
        print("UNSOLVABLE")
        return
    for i in range(10**len(S)):
        N = str(i).zfill(len(S))
        N = dict(zip(S, N))
        N1 = int("".join(N[s] for s in S1))
        N2 = int("".join(N[s] for s in S2))
        N3 = int("".join(N[s] for s in S3))
        if N1 + N2 == N3 and N[S1[0]] != "0" and N[S2[0]] != "0" and N[S3[0]] != "0":
            print(N1)
            print(N2)
            print(N3)
            return
    print("UNSOLVABLE")
main()

if __name__ == '__main__':
    main()