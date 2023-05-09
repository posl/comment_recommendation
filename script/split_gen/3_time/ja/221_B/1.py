def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        count = 0
        for i in range(len(S)):
            if S[i] != T[i]:
                count += 1
        if count == 2:
            print("Yes")
        else:
            print("No")
