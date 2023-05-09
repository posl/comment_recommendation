def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    if N > M:
        print("No")
        return
    if S == T:
        print("Yes")
        return
    for i in range(N):
        if S[i] == T[i]:
            continue
        else:
            if S[i] == T[i+1] and S[i+1] == T[i]:
                print("Yes")
                return
            else:
                print("No")
                return
    print("Yes")
    return
