def main():
    # Read data
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    # Find the second highest mountain
    max1 = -1
    max2 = -1
    for i in range(N):
        if max1 < T[i]:
            max2 = max1
            max1 = T[i]
        elif max2 < T[i]:
            max2 = T[i]
    # Find the name of the second highest mountain
    for i in range(N):
        if T[i] == max2:
            print(S[i])
            return

if __name__ == '__main__':
    main()