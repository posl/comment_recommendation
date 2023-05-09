def main():
    # read input
    N = int(input())
    S = str(input())
    # solve
    for i in range(1,N):
        S_i = S[:i]
        S_i_plus = S[i:]
        l = 0
        for j in range(1,N-i+1):
            if S_i[j-1] != S_i_plus[j-1]:
                l = j
        print(l)
    return None

if __name__ == '__main__':
    main()