def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S)):
            if S[i] == T[0]:
                if S[i:i+len(T)] == T:
                    print('Yes')
                    return
        print('No')
