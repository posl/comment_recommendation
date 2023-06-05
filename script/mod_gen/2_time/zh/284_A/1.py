def main():
    S = input()
    N = len(S)
    #print(N)
    #print(S)
    if N % 2 == 1:
        print("否")
        return
    else:
        for i in range(N):
            if S[i] == "(":
                pass
            elif S[i] == ")":
                pass
            else:
                print("否")
                return
        print("是")
        return
main()
