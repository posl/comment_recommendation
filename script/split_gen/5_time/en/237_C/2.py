def main():
    S = input()
    S_rev = S[::-1]
    for i in range(len(S)):
        if S[i] != S_rev[i]:
            print("No")
            break
    else:
        print("Yes")
