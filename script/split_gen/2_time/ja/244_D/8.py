def main():
    S = input().split()
    T = input().split()
    #print(S)
    #print(T)
    for i in range(3):
        if S[i] == T[i]:
            print("No")
            return
    print("Yes")
    return
