def main():
    S = input()
    T = input()
    #print(S,T)
    print(len(T) - max([len([1 for j in range(len(T)) if S[i+j] == T[j]]) for i in range(len(S)-len(T)+1)]))
