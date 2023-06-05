def main():
    S = input()
    l = len(S)
    for i in range(l//2):
        if S[i] != S[l-1-i]:
            print("No")
            return
    print("Yes")
main()
