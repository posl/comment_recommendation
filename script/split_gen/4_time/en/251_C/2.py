def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    #print(S)
    #print(T)
    best_score = 0
    best_index = 0
    for i in range(N):
        if T[i] > best_score:
            best_score = T[i]
            best_index = i
    print(best_index+1)
