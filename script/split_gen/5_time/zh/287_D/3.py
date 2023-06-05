def main():
    S = input()
    T = input()
    x = len(T)
    S = S.replace("?","")
    T = T.replace("?","")
    if x == 0:
        print("Yes")
        return
    if len(S) < x:
        print("No")
        return
    for i in range(len(S)-x+1):
        if S[i:i+x] == T:
            print("Yes")
            return
    print("No")
    return
