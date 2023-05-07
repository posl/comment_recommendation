def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S)):
            if S == T:
                print('Yes')
                break
            else:
                S = S[-1] + S[:-1]
        else:
            print('No')
