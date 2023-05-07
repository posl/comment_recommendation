def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = set(S1+S2+S3)
    if len(S) > 10:
        print("UNSOLVABLE")
        return
    N = list(range(10))
    for i in range(10**len(S)):
        for j in range(10**len(S)):
            for k in range(10**len(S)):
                if len(set(str(i)+str(j)+str(k))) == len(S):
                    if str(i)+str(j) == str(k):
                        if len(str(i)) == len(S1) and len(str(j)) == len(S2) and len(str(k)) == len(S3):
                            if check(S1, S2, S3, str(i), str(j), str(k)):
                                print(i)
                                print(j)
                                print(k)
                                return
    print("UNSOLVABLE")

if __name__ == '__main__':
    main()