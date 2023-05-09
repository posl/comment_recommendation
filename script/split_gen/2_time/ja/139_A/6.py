def main():
    S = input()
    T = input()
    #print(S)
    #print(T)
    count = 0
    for i in range(3):
        if S[i] == T[i]:
            count += 1
    print(count)
