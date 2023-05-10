def solve():
    S = input()
    T = input()
    min = len(T)
    for i in range(len(S)-len(T)+1):
        tmp = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                tmp += 1
        if min > tmp:
            min = tmp
    print(min)
