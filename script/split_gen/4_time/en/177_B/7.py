def main():
    S = input()
    T = input()
    min_change = len(T)
    for i in range(len(S) - len(T) + 1):
        change = 0
        for j in range(len(T)):
            if S[i + j] != T[j]:
                change += 1
        if change < min_change:
            min_change = change
    print(min_change)
