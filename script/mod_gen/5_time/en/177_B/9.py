def main():
    S = raw_input()
    T = raw_input()
    #print S, T
    min_change = 1000
    for i in range(len(S)-len(T)+1):
        #print S[i:i+len(T)]
        change = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                change += 1
        if min_change > change:
            min_change = change
    print min_change

if __name__ == '__main__':
    main()