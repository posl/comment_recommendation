def main():
    S = input()
    T = input()
    #print(S,T)
    count = 0
    i = 0
    while i < len(S):
        if S[i] != T[i]:
            count += 1
        i += 1
    print(count)
