def main():
    S = input()
    T = input()
    #print(S)
    #print(T)
    for i in range(len(S)):
        if ord(S[i]) - ord(T[i]) < 0:
            if ord(S[i]) - ord(T[i]) + 26 >= 0:
                continue
            else:
                print("No")
                return
        else:
            if ord(S[i]) - ord(T[i]) - 26 <= 0:
                continue
            else:
                print("No")
                return
    print("Yes")
    return
