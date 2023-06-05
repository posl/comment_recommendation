def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S1 = list(S1)
    S2 = list(S2)
    S3 = list(S3)
    S = list(set(S1+S2+S3))
    if len(S) > 10:
        print("UNSOLVABLE")
        return
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                N1 = []
                N2 = []
                N3 = []
                for s in S1:
                    if s == S[0]:
                        N1.append(str(i))
                    elif s == S[1]:
                        N1.append(str(j))
                    elif s == S[2]:
                        N1.append(str(k))
                for s in S2:
                    if s == S[0]:
                        N2.append(str(i))
                    elif s == S[1]:
                        N2.append(str(j))
                    elif s == S[2]:
                        N2.append(str(k))
                for s in S3:
                    if s == S[0]:
                        N3.append(str(i))
                    elif s == S[1]:
                        N3.append(str(j))
                    elif s == S[2]:
                        N3.append(str(k))
                if len(N1) == len(S1) and len(N2) == len(S2) and len(N3) == len(S3):
                    if int(''.join(N1)) + int(''.join(N2)) == int(''.join(N3)):
                        print(''.join(N1))
                        print(''.join(N2))
                        print(''.join(N3))
                        return
    print("UNSOLVABLE")
    return

if __name__ == '__main__':
    main()