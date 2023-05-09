def main():
    S = input().split()
    T = input().split()
    if S==T:
        print("Yes")
        return
    if S[0]==S[1] and T[0]==T[1]:
        print("Yes")
        return
    if S[0]==S[2] and T[0]==T[2]:
        print("Yes")
        return
    if S[1]==S[2] and T[1]==T[2]:
        print("Yes")
        return
    print("No")
    return
