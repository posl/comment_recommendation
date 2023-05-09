def main():
    #Read the first line.
    N = int(input())
    #Read the next N lines.
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    #Find the index of the second highest mountain.
    index_max = T.index(max(T))
    T[index_max] = 0
    index_second_max = T.index(max(T))
    #Print the name of the second highest mountain.
    print(S[index_second_max])

if __name__ == '__main__':
    main()