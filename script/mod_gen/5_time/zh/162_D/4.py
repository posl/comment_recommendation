def main():
    N = int(input())
    S = input()
    R = []
    G = []
    B = []
    for i in range(N):
        if S[i] == "R":
            R.append(i)
        elif S[i] == "G":
            G.append(i)
        else:
            B.append(i)
    ans = 0
    for i in range

if __name__ == '__main__':
    main()