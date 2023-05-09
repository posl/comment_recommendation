def main():
    S, K = input().split()
    K = int(K)
    S = list(S)
    S.sort()
    S2 = S.copy()
    S2.sort(reverse=True)
    S = "".join(S)
    S2 = "".join(S2)
    if K == 1:
        print(S)
    elif S == S2:
        print(S2)
    else:
        for i in range(K-1):
            S = next_permutation(S)
        print(S)

if __name__ == '__main__':
    main()