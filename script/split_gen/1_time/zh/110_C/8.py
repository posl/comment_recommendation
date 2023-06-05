def main():
    S = input()
    T = input()
    if len(set(S)) != len(set(T)):
        print("No")
        exit()
    if len(S) != len(T):
        print("No")
        exit()
    dic = {}
    for i in range(len(S)):
        if S[i] in dic:
            if dic[S[i]] != T[i]:
                print("No")
                exit()
        else:
            dic[S[i]] = T[i]
    print("Yes")
