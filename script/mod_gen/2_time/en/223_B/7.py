def main():
    #S = list(input())
    S = list("abracadabra")
    Smin = S[:]
    Smax = S[:]
    for i in range(len(S)):
        S.append(S.pop(0))
        Smin = min(Smin, S)
        Smax = max(Smax, S)
    print("".join(Smin))
    print("".join(Smax))
    print("".join(S))

if __name__ == '__main__':
    main()