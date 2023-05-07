def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    if len(set(S)) != N:
        print("No")
        return
    for s in S:
        if s[0] not in "HDCS":
            print("No")
            return
        if s[1] not in "A23456789TJQK":
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()