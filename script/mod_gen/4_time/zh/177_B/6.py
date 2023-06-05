def solve():
    S = input()
    T = input()
    min = len(T)
    for i in range(0, len(S)-len(T)+1):
        count = 0
        for j in range(0, len(T)):
            if(S[i+j] != T[j]):
                count += 1
        if(count < min):
            min = count
    print(min)
solve()
