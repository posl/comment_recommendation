def main():
    S1 = input()
    S2 = input()
    S3 = input()
    N1 = len(S1)
    N2 = len(S2)
    N3 = len(S3)
    if N1 < N2 or N1 < N3:
        print("UNSOLVABLE")
        return
    if N1 == N2:
        if N1 == N3:
            if S1 == S2 and S1 != S3:
                print("UNSOLVABLE")
                return
            if S1 != S2 and S1 == S3:
                print("UNSOLVABLE")
                return
            if S1 == S3 and S1 != S2:
                print("UNSOLVABLE")
                return
        else:
            if S1 == S2:
                print("UNSOLVABLE")
                return
    else:
        if N1 == N3:
            if S1 == S3:
                print("UNSOLVABLE")
                return
        else:
            if N2 == N3:
                if S2 == S3:
                    print("UNSOLVABLE")
                    return
    if N1 == N3:
        if N1 == N2:
            if S1 == S3 and S1 != S2:
                print("UNSOLVABLE")
                return
            if S1 != S3 and S1 == S2:
                print("UNSOLVABLE")
                return
            if S1 == S2 and S1 != S3:
                print("UNSOLVABLE")
                return
        else:
            if S1 == S3:
                print("UNSOLVABLE")
                return
    else:
        if N1 == N2:
            if S1 == S2:
                print("UNSOLVABLE")
                return
        else:
            if N2 == N3:
                if S2 == S3:
                    print("UNSOLVABLE")
                    return
    if N1 == N2:
        if N1 == N3:
            if S1 == S2 and S1 == S3:
                print("UNSOLVABLE")
                return
    else:
        if N1 == N3:
            if S1 == S3:
                print("UNSOLVABLE")
                return
        else:
            if N2 == N3:
                if S

if __name__ == '__main__':
    main()